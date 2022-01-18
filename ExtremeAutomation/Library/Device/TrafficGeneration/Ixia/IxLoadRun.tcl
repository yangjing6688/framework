############### Start TCL script ##################

package require IxLoadCsv
package require statCollectorUtils
set rep_name "E:\\_Support\\IxLoad\\TCLSample\\myrxf.rxf"

::IxLoad connect 127.0.0.1
if [catch {
#
# setup logger
set logtag "IxLoad-api"
set logName "reprun"
set logger [::IxLoad new ixLogger $logtag 1]
set logEngine [$logger getEngine]
$logEngine setLevels $::ixLogger(kLevelDebug) $::ixLogger(kLevelInfo)
$logEngine setFile $logName 4 2048 1
#-----------------------------------------------------------------------
# Create a test controller bound to the previosuly allocated # chassis chain. This will eventually run the test we created earlier.
#-----------------------------------------------------------------------
set testController [::IxLoad new ixTestController -outputDir 1]

set ResultDir "RESULTS\\reprun"
$testController setResultDir $ResultDir

set repository  [::IxLoad new ixRepository -name $rep_name]
set testName    [$repository testList(0).cget -name]
set test        [$repository testList.getItem $testName]

puts "Running test $testName of repository $rep_name"


  # Start the test
  $testController run $test -autorepository $testName.rxf

  vwait ::ixTestControllerMonitor
  puts $::ixTestControllerMonitor

}] {

    puts "Err running the tcl script"
}


#-----------------------------------------------------------------------
# Cleanup
#-----------------------------------------------------------------------

$testController releaseConfigWaitFinish
##########
### Generate Report
$testController generateReport \
	-detailedReport 1 \
	-format "HTML" \
	-testName "TCL Sample for Generate Report" \
	-testerName "Vasile Cirstea" \
	-dutName "No DUT" \
	-orientation "Portrait"

# -outputFile  #Path to which the test report is saved
# -mailTo "vcirstea@ixiacom.com   #Email address to which the report is automatically mailed after generation
# -highlights "Test" #Applies highlighting-style formatting all instances of the specified string in the report
# -coverPageImageFile Image file to be used as the report's cover page.

puts "The test ended. The report was generated"

::IxLoad delete $repository
::IxLoad delete $testController
::IxLoad delete $logger
::IxLoad delete $logEngine


#-----------------------------------------------------------------------
# Disconnect
#-----------------------------------------------------------------------
::IxLoad disconnect

puts " started ==== End ======== IxLoadRun finished"
############### End TCL script ##################
