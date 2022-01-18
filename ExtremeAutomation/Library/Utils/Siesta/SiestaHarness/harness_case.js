// Start Harness Configuration
var harnessConfig = {
    restServerIp: "127.0.0.1",
    restServerPort: 5000,
    restServerHttps: true,
    pollInterval: 500
    };
// End Harness Configuration

var testStepList = [];
var testStepUuids = [];
var completedStepUuids = [];
var testCompleted = false;
var testStepCompleted = true;
var globalReturnData = "";
var defaultTimeOut = 30000;
var waitForTimeout = defaultTimeOut;
var asyncFrame = null;
var interval = null;
var asyncKeepAlive = true;

StartTest(function(test) {
    test.diag("Running function StartTest");
    // Keeps the async frame open until the test is completed.
    asyncWatchDog(test);

    // Polls the rest server once a second for test step information.
    // Then executes each test step.
    // Will eventually report result information back to the rest server.
    pollAndExecuteSteps(test);

})

function asyncWatchDog(test) {
    test.diag("Running function asyncWatchDog");
    // Starts a new async frame with a timeout of 3 seconds.
    // After 2 seconds it stops the async frame and starts another with a 3 second timeout.
    // Unless the test case has been marked as completed, then no new async frame is started.
    var asyncTimeout = 3000;

    asyncFrame = test.beginAsync(asyncTimeout);

    var asyncInterval = setInterval(function () {
        test.endAsync(asyncFrame);

        if (asyncKeepAlive === true) {
            asyncFrame = test.beginAsync(asyncTimeout);
        }
    }, 2000)
}

function pollAndExecuteSteps(test) {
    test.diag("Running function pollAndExecuteSteps");
    // Polls the rest server once per second.
    // Passes the retrieved data to updateStepList which adds any new steps to the step lists.
    // Then executes the oldest test step.
    // Currently this repeats for <timeout> seconds in the future a stop test test step will be sent
    // via the rest server.
    interval = setInterval(function() {
        getAndExecuteStep(test);
    }, harnessConfig.pollInterval)
}

function getAndExecuteStep(test) {
    test.diag("Running function getAndExecuteStep");
    if (testStepCompleted === true) {
        if (testCompleted === true) {
            test.diag("Stopping harness...");
            clearInterval(interval);
            asyncKeepAlive = false;
            test.endAsync(asyncFrame);
            test.exit();
        }

        try {
            testStepCompleted = false;
            var testStepData = getDataFromRestServer(test, function() {});
            updateStepLists(test, testStepData);
            executeSingleTestStep(test, testStepUuids[0]);
        }
        catch (err) {
            // If we receive an unknown exception kill the harness.
            if (err.message.indexOf("Ext") > -1) {
                testStepCompleted = true;
                testCompleted = true;
                throw(err);
            }
            else if (err.name === "NetworkError") {
                test.diag("Unable to reach rest server, retrying...");
                testStepCompleted = true;
            }
            else if (err.name !== "TypeError") {
                testStepCompleted = true;
                testCompleted = true;
                throw(err);
            }
            else {
                testStepCompleted = true;
            }
        }
    }
    else {
        test.diag("Waiting for test step to finish execution...")
    }
}

function getRestUrl(update) {
    var restUrl = "";

    if (harnessConfig.restServerHttps === true) {
        restUrl += "https://"
    }
    else {
        restUrl += "http://"
    }

    if (update === true) {
        restUrl += harnessConfig.restServerIp + ":" + harnessConfig.restServerPort + "/siesta/v1/test_step"
    }
    else {
        restUrl += harnessConfig.restServerIp + ":" + harnessConfig.restServerPort + "/siesta/v1/unrun_test_steps"
    }

    return restUrl
}

function getDataFromRestServer(test) {
    test.diag("Running function getDataFromRestServer");
    // Creates an XMLHttpRequest and sends the request to the local REST server for test step information.
    // Returns the parsed JSON information.
    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", getRestUrl(false), false);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.send();

    return JSON.parse(xhttp.responseText)
}

function markStepAsCompleted(test, stepUuid, result) {
    test.diag("Running function markStepAsCompleted");
    // Creates and XMLHttpRequest to post updated test step information to the rest server.
    // Adds the completed step UUID to the completedStepUuid list.
    var xhttp = new XMLHttpRequest();

    var returnDataInfo = getReturnDataInfo(test);
    var returnData = returnDataInfo["data"];
    var returnDataType = returnDataInfo["type"];

    var data = {"id": stepUuid,
                "completed": true,
                "return_data": returnData,
                "return_data_type": returnDataType,
                "step_result": result
                };

    xhttp.open("POST", getRestUrl(true), false);
    xhttp.setRequestHeader("Content-type", "application/json");

    try {
        xhttp.send(JSON.stringify(data));
        completedStepUuids.push(stepUuid);
        globalReturnData = "";
        return true;
    }
    catch (err) {
        return false;
    }

}

function getReturnDataInfo(test) {
    test.diag("Running function getReturnDataInfo");
    // This function checks the return data to make sure it's a valid type.
    returnDict = {};

    if (typeof(globalReturnData) === "string") {
        returnDict["data"] = globalReturnData;
        returnDict["type"] = "str";
    }
    else if (typeof(globalReturnData) === "number") {
        returnDict["data"] = globalReturnData.toString();
        if (returnDict["data"].indexOf(".") != -1) {
            returnDict["type"] = "float";
        }
        else {
            returnDict["type"] = "int";
        }
    }
    else if (typeof(globalReturnData) === "boolean") {
        returnDict["data"] = globalReturnData.toString();
        returnDict["type"] = "bool";
    }
    else if (globalReturnData == null) {
        returnDict["data"] = "";
        returnDict["type"] = "None";
    }
    else {
        returnDict["data"] = "The component query did not return a string, number, boolean, or null(None).";
        returnDict["type"] = "Unknown";
    }

    return returnDict;
}

function updateStepLists(test, testStepJson) {
    test.diag("Running function updateStepLists");
    // Iterate over the received JSON data.
    // Check if the step has been marked as completed, if it has ignore it.
    // Check if the step's UUID has already been added to the testStepUuid list, if it has
    // ignore it.
    // Otherwise add the test step to the testStepList and the step's UUID to the
    // testStepUuid list.
    for (i = 0; i < testStepJson.test_steps.length; i++) {
        var step = testStepJson.test_steps[i];

        if (completedStepUuids.indexOf(step.id) === -1) {
            if (testStepUuids.indexOf(step.id) === -1) {
                testStepList.push(step);
                testStepUuids.push(step.id);
            }
        }
    }
}

function executeSingleTestStep(test, testStepUuid) {
    test.diag("Running function executeSingleTestStep");
    // Gets the test step data using the steps UUID.
    // If the test step data is "STOP_HARNESS" mark the test as completed.
    // Otherwise generate the list of chain commands to send to the page.
    // Then execute the chain commands.
    // Finally mark the step as completed and remove it from the step list.
    var testStepData = testStepList[testStepUuids.indexOf(testStepUuid)].data;

    if (testStepData === "STOP_HARNESS") {
        testCompleted = true;
    }
    else {
        testStepCompleted = false;
        var chainCommands = createChainList(test, testStepData, testStepUuid);
        executeChainCommandList(test, testStepUuid, chainCommands);
    }
}

function createChainList(test, testStepData, testStepUuid) {
    test.diag("Running function createChainList");
    // This function creates the list of chain commands that will be executed later.
    // The supported command types are as follows.
    //  - click
    //  - rightclick
    //  - type
    //  - delay
    //  - waitFor
    //  - doubleclick
    //  - componentquery
    //  - movecursorto
    //  - screenshot
    //  - emc_util*
    //  - emc_util_wait_for*
    //
    // The chainDict format follows the Siesta API and can differ between each action.
    // https://www.bryntum.com/docs/siesta/#!/api/Siesta.Test.Action
    //
    // * - These command types not found in the siesta documentation.

    var chainList = [];

    for (i = 0; i < testStepData.length; i++) {
        var chainDict = {};

        if ("timeout" in testStepData[i]) {
            test.waitForTimeout = testStepData[i].timeout;
            waitForTimeout = testStepData[i].timeout;
        }
        else {
            test.waitForTimeout = defaultTimeOut;
            waitForTimeout = defaultTimeOut;
        }

        if (testStepData[i].action.toLowerCase() === "click") {
            chainDict.action = "click";
            chainDict.target = testStepData[i].target;
        }
        else if (testStepData[i].action.toLowerCase() === "rightclick") {
            chainDict.action = "rightclick";
            chainDict.target = testStepData[i].target;
        }
        else if (testStepData[i].action.toLowerCase() === "mousedown") {
            chainDict.action = "mouseDown";
            chainDict.target = testStepData[i].target;
        }
        else if (testStepData[i].action.toLowerCase() === "mouseup") {
            chainDict.action = "mouseUp";
            chainDict.target = testStepData[i].target;
        }
        else if (testStepData[i].action.toLowerCase() === "type") {
            chainDict.action = "type";

            if (testStepData[i].target !== null) {
                chainDict.target = testStepData[i].target;
            }

            chainDict.text = testStepData[i].text;
            chainDict.clearExisting = testStepData[i].clear_existing
        }
        else if (testStepData[i].action.toLowerCase() === "delay") {
            chainDict.waitFor = testStepData[i].delay;
        }
        else if (testStepData[i].action.toLowerCase() === "waitfor") {
            chainDict.waitFor = "PageLoad"
            var trigger = testStepData[i].trigger;
            var target = testStepData[i].target;
            var trigger_dict = {};
            trigger_dict[trigger] = target;
            chainDict.trigger = trigger_dict;
        }
        else if (testStepData[i].action.toLowerCase() === "doubleclick") {
            chainDict.action = "doubleclick";
            chainDict.target = testStepData[i].target;
        }
        else if (testStepData[i].action.toLowerCase() === "componentquery") {
            query = "test.global.Ext.ComponentQuery.query('" + testStepData[i].target + "')" + testStepData[i].args + ";"
            chainDict = function(next) {
                try {
                    globalReturnData = eval(query);
                }
                catch (err) {
                    globalReturnData = "component query failed"
                    markStepAsCompleted(test, testStepUuid, false);
                    removeCompletedSteps(test, testStepUuid);
                    clearTimeout(testStepTimeout);
                    testStepCompleted = true;
                }
                next();
            }
            chainList.push(chainDict);
        }
        else if (testStepData[i].action.toLowerCase() === "queryselector") {
            query = "test.global.document.querySelector('" + testStepData[i].target + "')" + testStepData[i].args + ";"
            chainDict = function(next) {
                try {
                    globalReturnData = eval(query);
                }
                catch (err) {
                    globalReturnData = "document query failed"
                    markStepAsCompleted(test, testStepUuid, false);
                    removeCompletedSteps(test, testStepUuid);
                    clearTimeout(testStepTimeout);
                    testStepCompleted = true;
                }
                if (globalReturnData != null) {
                    globalReturnData = globalReturnData.outerHTML;
                }
                next();
            }
            chainList.push(chainDict);
        }
        else if (testStepData[i].action.toLowerCase() === "movecursorto") {
            if (testStepData[i].by !== undefined) {
                chainDict.action = "movecursor";
                chainDict.by = testStepData[i].by;
            } else {
                chainDict.action = "movecursorto";
                chainDict.target = testStepData[i].target;
            }
        }
        else if (testStepData[i].action.toLowerCase() === "screenshot") {
            chainDict.screenshot = testStepData[i].file_name;
        }
        else if (testStepData[i].action.toLowerCase() === "emc_util") {
            var util_func = testStepData[i].function_name;
            var util_args = formatUtilArgs(testStepData[i].function_args);
            var func_call = "test." + util_func + "(" + util_args + ");"

            chainDict = function(next) {
                globalReturnData = eval(func_call);
                next();
            }
            chainList.push(chainDict);
        }
        else if (testStepData[i].action.toLowerCase() === "emc_util_wait_for") {
            var util_func = testStepData[i].function_name;
            chainDict[util_func] = testStepData[i].function_args;
            chainDict["timeout"] = testStepData[i].timeout;
        }

        if ("options" in testStepData[i]) {
            chainDict.options = testStepData[i].options;
        }

        if (Object.keys(chainDict).length > 0) {
            chainList.push(chainDict);
        }
    }
    return chainList
}

function executeChainCommandList(test, testStepUuid, chainCommandList) {
    test.diag("Running function executeChainCommandList with UUID " + testStepUuid);
    // Execute each chain command found in the chainCommandList. If the chain command is successful
    // testStepCompleted will be marked as true and the REST server will be updated with step_result set to True.
    // If the chain command is unsuccessful testStepCompleted will be set to True but the REST server step_result
    // will be marked False.
    testStepTimeout = null;
    intervalCounter = 0;

    test.diag("Starting chain with step " + testStepUuid);
    test.chain(
        function(next) {   // Start the testStepTimeout.
            testStepTimeout = startStepTimeout(test, testStepUuid);
            next();
        },
        chainCommandList,  // Execute the chain commands.
        function() {       // Call back if the chain was successful.
            if (testStepCompleted === false) {
                test.diag("Finished sub test chain with UUID " + testStepUuid);
                updateStepInterval = setInterval(function() {
                    result = markStepAsCompleted(test, testStepUuid, true);

                    if (intervalCounter > 60) {
                        clearInterval(updateStepInterval);
                        throw(Error("Rest server was not reachable..."));
                    }

                    if (result === true) {
                        removeCompletedSteps(test, testStepUuid);
                        test.diag("Executed step: " + testStepUuid);
                        clearTimeout(testStepTimeout);
                        testStepCompleted = true;
                        clearInterval(updateStepInterval);
                    }
                    else {
                        intervalCounter += 1;
                        clearTimeout(testStepTimeout);
                        testStepTimeout = startStepTimeout(test, testStepUuid);
                        test.diag("Unable to update test step, retrying...");
                    }
                }, 1000)
            }
        }
    );
}

function startStepTimeout(test, testStepUuid) {
    //
    stepTimeout = 60 * 1000  // Timeout is in milliseconds.
    test.diag("Starting step timeout");

    timeout = setTimeout(function() {
        if (testStepCompleted === false) {
            markStepAsCompleted(test, testStepUuid, false);
            removeCompletedSteps(test, testStepUuid);
            test.diag("Failed to execute step: " + testStepUuid);
            testStepCompleted = true;
        }
    }, stepTimeout);

    return timeout;
}

function removeCompletedSteps(test, completedUuid) {
    test.diag("Running function RemoveCompletedSteps");
    // Iterate over each item in the completedSteps list.
    // Remove the corresponding test case from the testStepList and the testStepUuid list.
    // Reset completedStepUuids to an empty list.
    for (i = 0; i < completedStepUuids.length; i++) {
        testStepList.splice(testStepUuids.indexOf(completedStepUuids[i]), 1);
        testStepUuids.splice(testStepUuids.indexOf(completedStepUuids[i]), 1);
    }
}

function getTimeStamp() {
    test.diag("Running function getTimeStamp");
    // This function creates a time stamp to be used when taking screen shots.
    // The format is HH-MM-SS_YYYY-MM-DD
    var date = new Date();

    var year = date.getUTCFullYear();
    var month = date.getUTCMonth();
    var day = date.getUTCDate();
    var hour = date.getHours();
    var minute = date.getMinutes();
    var second = date.getSeconds();

    month = ("0" + (month + 1)).slice(-2);
    day = ("0" + day).slice(-2);
    hour = ("0" + hour).slice(-2);
    minute = ("0" + minute).slice(-2);
    second = ("0" + second).slice(-2);

    var timeStamp = hour + "-" + minute + "-" + second + "-" + year + "-" + month + "-" + day;

    return timeStamp;
}

function formatUtilArgs(argList) {
    var arg_str = "";
    for (j = 0; j < argList.length; j++) {
        if (j == argList.length - 1) {
            arg_str += "'" + argList[j].replace(/'/g, '"') + "'";
        }
        else {
            arg_str += "'" + argList[j].replace(/'/g, '"') + "', ";
        }
    }
    return arg_str;
}
