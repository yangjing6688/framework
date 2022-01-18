@ECHO OFF

SET TEST_DIR="..\.."
SET REPORT_DIR="reports"

:: Remove old reports
IF EXIST %REPORT_DIR% (
    rmdir /S /Q %REPORT_DIR%
)

REM python %TEST_DIR%\PythonTests\AgentTests\AgentTests.py %REPORT_DIR%
REM python %TEST_DIR%\PythonTests\AgentTests\RestTests.py %REPORT_DIR%
REM python %TEST_DIR%\PythonTests\AgentTests\SnmpTests.py %REPORT_DIR%
REM python %TEST_DIR%\PythonTests\AgentTests\SshTests.py %REPORT_DIR%
REM python %TEST_DIR%\PythonTests\AgentTests\TelnetTests.py %REPORT_DIR%

python %TEST_DIR%\PythonTests\ApiTests\ApiUnitTests.py %REPORT_DIR%
python %TEST_DIR%\PythonTests\ApiTests\ApiLoadTests.py %REPORT_DIR%

python %TEST_DIR%\PythonTests\KeywordApiTests\CliApiTests.py %REPORT_DIR%
python %TEST_DIR%\PythonTests\KeywordApiTests\RestApiTests.py %REPORT_DIR%
python %TEST_DIR%\PythonTests\KeywordApiTests\SnmpApiTests.py %REPORT_DIR%

python %TEST_DIR%\PythonTests\KeywordTests\CliKeywordTests.py %REPORT_DIR%

python %TEST_DIR%\PythonTests\LibraryTests\InspectionToolkitTests.py %REPORT_DIR%
python %TEST_DIR%\PythonTests\LibraryTests\LoggerTests.py %REPORT_DIR%
python %TEST_DIR%\PythonTests\LibraryTests\ParseWrapperTests.py %REPORT_DIR%
python %TEST_DIR%\PythonTests\LibraryTests\PortParserTests.py %REPORT_DIR%
python %TEST_DIR%\PythonTests\LibraryTests\PromptHandlerTests.py %REPORT_DIR%

python %TEST_DIR%\PythonTests\TrafficGenTests\ArpResolutionTests.py %REPORT_DIR%
:: This cannot be run until ostinato is updated.
:: python %TEST_DIR%\PythonTests\TrafficGenTests\TrafficGenerationTests.py %REPORT_DIR%

python %TEST_DIR%\PythonTests\UtilTests\GlobalVariableCacheTests.py %REPORT_DIR%
python %TEST_DIR%\PythonTests\UtilTests\MultiauthSessionTests.py %REPORT_DIR%
python %TEST_DIR%\PythonTests\UtilTests\PlatVarTests.py %REPORT_DIR%
python %TEST_DIR%\PythonTests\UtilTests\ValueStorageTests.py %REPORT_DIR%
python %TEST_DIR%\PythonTests\KeywordTests\CliKeywordTests.py %REPORT_DIR%

:: Parse the results.
python %TEST_DIR%\Utilities\QuickParseResults.py %REPORT_DIR% %REPORT_DIR%\..\
