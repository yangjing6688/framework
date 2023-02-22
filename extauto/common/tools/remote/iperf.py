import subprocess
import sys
import re
import os
import signal
from time import sleep
from robot.utils import asserts
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger
from robot.output import librarylogger

def write(msg, level='INFO', html=False):
    print(msg)
    librarylogger.write(msg, level, html)
    with open('log.txt', 'a') as f:
        print(f'{level}\tHH:MM:SS > {msg}', file=f)
logger.write = write

class MuIPerf(object):
    def __init__(self):
        """
        EXAMPLE USAGE - iperf3 must be installed on all MUs.
        NOTE:  expected Tx Rx is always in bits or bytes per second. Even if iperf is in K,M or Gig
            ${svrpid}=    mu1.Start Iperf Server      # Start server on remote MU
            SET GLOBAL VARIABLE    ${svrpid}
            LOG TO CONSOLE   Iperf server pid is ${svrpid}
            ${client}=    mu2.Start Iperf Client   ${mu1.wifiip}  expRxRate=100000
            LOG TO CONSOLE   ${client}
            ## IN SETTINGS  (safety iperf server clean up. Lives forever if never rx traffic)
                [Teardown]   mu1.Kill Iperf Server   ${svrpid}
        """
        self.puts = True
        pass

    def kill_iperf_server(self, spid, timeout=None):
        """
        Runs in 2 modes.  First (safety) is forked by server start and will kill the server after
        timeout.  2nd is a general cleanup in case the client is not able to reach the server
        :param spid: server process id
        :param timeout: delay timeout seconds then kill
        """
        if timeout:
            sleep(timeout)
        if os.name == 'nt':
            try:
                os.system(f"taskkill /pid {spid} /F")
            except Exception as e:
                logger.info(f"NT Kill CtrlC Failed: {e}")
                pass
            try:
                os.system("taskkill /im iperf3.exe /F")
            except Exception as e:
                logger.info(f"NT Kill CtrlBrk Failed: {e}")
                pass
        else:
            try:
                os.killpg(os.getpgid(spid), signal.SIGTERM)
            except Exception:
                pass

    def start_iperf_server(self, format=None, port=None, multiuse=None):
        """
        Start the iperf3 server
        iperf3 -s -f K -t 180 -1
        :param format: k, m, g for Kbits, Mbits, Gbits or K, M, G for KBytes, Mbytes, Gbytes
        :param port: default 5201 if None.  Alter if port is in use
        :param multiuse: default None.  If set the server will stay up for 180 seconds
        :return:
        """
        legalRates = ['k','m','g','K','M','G']
        # Commented on 1/18/23 because it is unused
        # fPart = ''
        if format:
            if str(format) not in legalRates:
                logger.info(f'{format} is not a valid rate. Try: {legalRates}')
                sys.exit()
        # Commented on 1/18/23 because it is unused
        #     fPart = f' -f {str(format)}'
        # pPart = ''
        # if port:
        #     pPart = f' -p {port}'
        mPart=' --one-off'
        if multiuse:
            mPart=''
        cmd = f'iperf3 -s -f {format}{mPart}'
        BuiltIn().log_to_console(f"Start IPerf3 Server: {cmd}")
        process = subprocess.Popen(cmd, start_new_session=True)
        return process.pid

        # if os.name == 'nt':
        #     try:
        #         os.system(f"taskkill /pid {process.pid} /F")
        #     except Exception as e:
        #         logger.info(f"NT Kill CtrlC Failed: {e}")
        #         pass
        #     try:
        #         os.system("taskkill /im iperf3.exe /F")
        #     except Exception as e:
        #         logger.info(f"NT Kill CtrlBrk Failed: {e}")
        #         pass


    def start_iperf_client(self, host, expTxRate=None, expRxRate=None,
                           format='K', tcpWinSize=None, bidir=None, reverse=None, port=None, prt_local=None):
        """
        Start the iperf3 server
        iperf3 -c 192.168.10.1 -f K -w 500K -R
        :param host:  ip address or hostname of server
        :param expTxRate:  expect sender rate at the given Kbits,Mbits,KBytes,MBytes
        :param expRxRate:  expect receiver rate at the given Kbits,Mbits,KBytes,MBytes
        :param format: k, m, g for Kbits, Mbits, Gbits or K, M, G for KBytes, Mbytes, Gbytes
        :param tcpWinSize: TCP window size  ex 100K  or 500K
        :param bidir: test bidirectional.
        :param reverse: boolean or passing this arg, non-None will measure from server to client
        :param port: default 5201 if None.  Alter if port is in use
        :param prt_local: print output from server side on the client side. If true print server output on client
        :return:
        """
        # Commented on 1/18/23 because it is unused
        # legalRates = ['k', 'm', 'g', 'K', 'M', 'G']
        fPart = f'-f {format}'
        wPart = ''
        if tcpWinSize:
            wPart = f' -w {tcpWinSize}'
        biPart = ''
        if bidir:
            biPart = ' -d'
        rPart = ''
        if reverse:
            rPart = ' -R'
        pPart = ''
        if port:
            pPart = f' -p {port}'
        pLocal = ''
        if prt_local:
            pLocal = ' --get-server-output'

        cmd = f'iperf3 -c {host} {fPart}{wPart}{biPart}{rPart}{pPart}{pLocal}'
        process = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        cmd_out = []
        i = 0
        avg = 0.0
        tffcAvg = 0
        # Commented on 1/18/23 because it is unused
        # tString = ''
        sStr = ""
        rStr = ""
        tx = 0
        rx = 0
        txrate = 0
        rxrate = 0
        aStr = ""
        label = 'bits/sec'
        anyFail = 0
        if self.puts:
            print('IPERF Client Started')

        tffc = re.compile(r"sec[ ]+[0-9\.]+ [a-zA-Z]+[ ]+([0-9\.]+) ([a-zA-Z]+\/sec)$")
        sndr = re.compile(r"sec[ ]+[0-9\.]+ [a-zA-Z]+[ ]+([0-9\.]+) ([a-zA-Z]+\/sec)[ ]+sender")
        rcvr = re.compile(r"sec[ ]+[0-9\.]+ [a-zA-Z]+[ ]+([0-9\.]+) ([a-zA-Z]+\/sec)[ ]+receiver")
        labRe = re.compile(r"Bytes.*")
        for line in process.stdout:
            hitTffc = tffc.search(line.decode().strip())
            sndrOut = sndr.search(line.decode().strip())
            rcvrOut = rcvr.search(line.decode().strip())
            if hitTffc:
                if hitTffc.group(2) == 'Kbits/sec' or hitTffc.group(2) == 'KBytes/sec':
                    rate = float(hitTffc.group(1)) * 1000
                    avg = avg + rate
                    i += 1
                elif hitTffc.group(2) == 'Mbits/sec' or hitTffc.group(2) == 'MBytes/sec':
                    rate = float(hitTffc.group(1)) * 1000000
                    avg = avg + rate
                    i += 1
                elif hitTffc.group(2) == 'Gbits/sec' or hitTffc.group(2) == 'GBytes/sec':
                    rate = float(hitTffc.group(1)) * 1000000000
                    avg = avg + rate
                    i += 1
                else:
                    rate = float(hitTffc.group(1))
                    avg = avg + rate
                    i += 1
                if labRe.search(hitTffc.group(2)):
                    label = 'Bytes/sec'
                else:
                    label = 'bits/sec'
            if self.puts:
                print(line.decode().strip())
            cmd_out.append(line.decode().strip())
            if sndrOut:
                tx = float(sndrOut.group(1))
                if sndrOut.group(2) == 'Kbits/sec' or sndrOut.group(2) == 'KBytes/sec':
                    txrate = tx * 1000
                elif sndrOut.group(2) == 'Mbits/sec' or sndrOut.group(2) == 'MBytes/sec':
                    txrate = tx * 1000000
                elif sndrOut.group(2) == 'Gbits/sec' or sndrOut.group(2) == 'GBytes/sec':
                    txrate = tx * 1000000000
                else:
                    txrate = tx
                if labRe.search(sndrOut.group(2)):
                    tlabel = 'Bytes/sec'
                else:
                    tlabel = 'bits/sec'
                sStr = f"Sender:{int(txrate)} {tlabel}"
            if rcvrOut:
                print('Hit IPERF3 Run End.')
                rx = float(rcvrOut.group(1))
                if rcvrOut.group(2) == 'Kbits/sec' or rcvrOut.group(2) == 'KBytes/sec':
                    rxrate = rx * 1000
                elif rcvrOut.group(2) == 'Mbits/sec' or rcvrOut.group(2) == 'MBytes/sec':
                    rxrate = rx * 1000000
                elif rcvrOut.group(2) == 'Gbits/sec' or rcvrOut.group(2) == 'GBytes/sec':
                    rxrate = rx * 1000000000
                else:
                    rxrate = rx
                if labRe.search(rcvrOut.group(2)):
                    rlabel = 'Bytes/sec'
                else:
                    rlabel = 'bits/sec'
                sStr = f"Sender:{int(float(txrate))} {tlabel}"
                rStr = f"Receiver:{int(float(rxrate))} {rlabel}"
                if i > 0:
                    tffcAvg = int(float(avg) / float(i))
                    aStr = f"Avg:{tffcAvg} {label}"
                emsg = ''
                if expTxRate:
                    try:
                        msg = f'Sender rate {int(float(txrate))} should be greater than {expTxRate}'
                        asserts.assert_false(int(float(txrate)) <= int(float(expTxRate)), msg)
                    except AssertionError as e:
                        emsg = f"{emsg}{msg}"
                        anyFail = 1
                        print(e)
                    except Exception:
                        pass

                if expRxRate:
                    try:
                        msg = f"Receiver rate {int(float(rxrate))} should be greater than {expRxRate}"
                        asserts.assert_false(int(float(rxrate)) <= int(float(expRxRate)), msg)
                    except AssertionError as e:
                        emsg = f"{emsg}\n{msg}"
                        anyFail = 1
                        print(e)
                    except Exception:
                        pass
                # Commented on 1/18/23 because it is unused
                # ipOut = '\n'.join(cmd_out)
                BuiltIn().should_be_true(anyFail == 0, emsg)
                return f"Results:\nexpTx:{expTxRate} actual:{sStr}\nexpRx:{expRxRate} actual:{rStr}\n{aStr}\nanyFail:{anyFail}"
        return -1

if __name__ == "__main__":
    obj = MuIPerf()
    output = obj.start_iperf_client('10.69.61.101', expTxRate=10000000, expRxRate=10000000)
    print(output)
