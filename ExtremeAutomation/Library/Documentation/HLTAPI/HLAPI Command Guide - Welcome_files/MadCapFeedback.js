/// <reference path="jquery.js" />
/// <reference path="MadCapGlobal.js" />
/// <reference path="MadCapUtilities.js" />
/// <reference path="MadCapDom.js" />
/// <reference path="MadCapXhr.js" />

/*!
* Copyright MadCap Software
* http://www.madcapsoftware.com/
*
* v9.0.0.0
*/

(function () {
    MadCap.WebHelp = MadCap.CreateNamespace("WebHelp");

    MadCap.WebHelp.FeedbackController = function (server) {
        if (MadCap.WebHelp.FeedbackController.Shared != null)
            return MadCap.WebHelp.FeedbackController.Shared;

        MadCap.WebHelp.FeedbackController.Shared = this;

        //

        var _Init = false;
        var _Initializing = false;
        var _InitOnCompleteFuncs = new Array();
        var _LiveHelpScriptIndex = 0;
        var _Self = this;
        var _InitTimeout = 3000;

        this.Server = server;
        this.FeedbackServer = _GetFeedbackServerUrl(server);
        this.Version = -1;
        this.FeedbackActive = false;
        this.PulseServer = null;
        this.PulseEnabled = false;
        this.PulseActive = false;
        this.PulseUserGuid = null;

        function _InitComplete() {
            for (var i = 0; i < _InitOnCompleteFuncs.length; i++)
                _InitOnCompleteFuncs[i](_Self);

            _Init = true;
        }

        function _GetFeedbackServerUrl(server, prefix) {
            if (server == null)
                return null;

            if (typeof prefix == 'undefined')
                prefix = "";

            var serverUrl = new MadCap.Utilities.Url(server);
            serverUrl = serverUrl.CombinePath(prefix + "Service.FeedbackExplorer/FeedbackJsonService.asmx/");

            return serverUrl.FullPath;
        }

        function _AddScriptTag(webMethodName, OnCompleteFuncName, nameValuePairs, url) {
            var script = document.createElement("script");
            var head = document.getElementsByTagName("head")[0];
            var scriptID = "MCLiveHelpScript_" + _LiveHelpScriptIndex++;
            var src = _Self.FeedbackServer + webMethodName + "?";

            src += "OnComplete=" + OnCompleteFuncName + "&ScriptID=" + scriptID + "&UniqueID=" + (new Date()).getTime();

            if (nameValuePairs != null) {
                for (var i = 0, length = nameValuePairs.length; i < length; i++) {
                    var pair = nameValuePairs[i];
                    var name = pair[0];
                    var value = encodeURIComponent(pair[1]);

                    src += ("&" + name + "=" + value);
                }
            }

            if (document.body.currentStyle != null) {
                var ieUrlLimit = 2083;

                if (src.length > ieUrlLimit) {
                    var diff = src.length - ieUrlLimit;
                    var data = { ExceedAmount: diff };
                    var ex = new MadCap.FeedbackException(-1, "URL limit exceeded.", data);

                    throw ex;
                }
            }

            var qsLimit = 2048;
            var qsPos = src.indexOf("?")
            var qsChars = src.substring(qsPos + 1).length;

            if (qsChars > qsLimit) {
                var diff = qsChars - qsLimit;
                var data = { ExceedAmount: diff };
                var ex = new MadCap.FeedbackException(-1, "Query string limit exceeded.", data);

                throw ex;
            }

            script.id = scriptID;
            script.setAttribute("type", "text/javascript");
            script.setAttribute("src", src);

            head.appendChild(script);

            return scriptID;
        }

        function _RemoveScriptTag(scriptID) {
            // IE bug: Need this setTimeout() or else IE will crash. This happens when removing the <script> tag after re-navigating to the same page.

            window.setTimeout(function () {
                var script = document.getElementById(scriptID);

                script.parentNode.removeChild(script);
            }, 10);
        }

        this.Init = function (OnCompleteFunc) {
            if (_Init) {
                OnCompleteFunc(this);
                return;
            }

            if (OnCompleteFunc != null)
                _InitOnCompleteFuncs.push(OnCompleteFunc);

            if (_Initializing)
                return;

            _Initializing = true;

            _Self.GetVersion(function () {
                if (_Self.PulseEnabled)
                    _Self.GetPulseServerActivated(function (active) {
                        _Self.PulseActive = active && active.toLowerCase() === 'true';

                        _InitComplete();
                    });
                else
                    _InitComplete();
            });

            window.setTimeout(function () {
                if (!_Init)
                    _InitComplete();
            }, _InitTimeout);
        }

        this.GetUserGuid = function () {
            return _Self.PulseEnabled ? _Self.PulseUserGuid : MadCap.Utilities.Store.getItem("LiveHelpUserGuid");
        }

        this.LogTopic = function (topicID, cshID, OnCompleteFunc) {
            this.LogTopicOnComplete = function (scriptID) {
                if (OnCompleteFunc != null)
                    OnCompleteFunc();

                //

                _RemoveScriptTag(scriptID);

                this.LogTopicOnComplete = null;
            };

            this.GetVersion(function (version) {
                if (version == 1) {
                    _AddScriptTag("LogTopic", "MadCap.WebHelp.FeedbackController.Shared.LogTopicOnComplete", [["TopicID", topicID]]);
                }
                else {
                    _AddScriptTag("LogTopic2", "MadCap.WebHelp.FeedbackController.Shared.LogTopicOnComplete", [["TopicID", topicID],
                                                                                                        ["CSHID", cshID]]);
                }
            });
        };

        this.LogSearch = function (projectID, userGuid, resultCount, language, query) {
            this.LogSearchOnComplete = function (scriptID) {
                _RemoveScriptTag(scriptID);

                this.LogSearchOnComplete = null;
            }

            _AddScriptTag("LogSearch", "MadCap.WebHelp.FeedbackController.Shared.LogSearchOnComplete", [["ProjectID", projectID],
                                                                                                 ["UserGuid", userGuid],
                                                                                                 ["ResultCount", resultCount],
                                                                                                 ["Language", language],
                                                                                                 ["Query", query]]);
        };

        this.AddComment = function (topicID, userGuid, userName, subject, comment, parentCommentID, OnCompleteFunc) {
            this.AddCommentOnComplete = function (scriptID) {
                if (OnCompleteFunc != null)
                    OnCompleteFunc();

                //

                _RemoveScriptTag(scriptID);

                this.AddCommentOnComplete = null;
            }

            _AddScriptTag("AddComment", "MadCap.WebHelp.FeedbackController.Shared.AddCommentOnComplete", [["TopicID", topicID],
                                                                                                   ["UserGuid", userGuid],
                                                                                                   ["Username", userName],
                                                                                                   ["Subject", subject],
                                                                                                   ["Comment", comment],
                                                                                                   ["ParentCommentID", parentCommentID]]);
        };

        this.GetAverageRating = function (topicID, OnCompleteFunc, onCompleteArgs) {
            this.GetAverageRatingOnComplete = function (scriptID, averageRating, ratingCount) {
                if (OnCompleteFunc != null)
                    OnCompleteFunc(averageRating, ratingCount, onCompleteArgs);

                //

                _RemoveScriptTag(scriptID);

                this.GetAverageRatingOnComplete = null;
            };

            _AddScriptTag("GetAverageRating", "MadCap.WebHelp.FeedbackController.Shared.GetAverageRatingOnComplete", [["TopicID", topicID]]);
        };

        this.SubmitRating = function (topicID, rating, comment, OnCompleteFunc, onCompleteArgs) {
            this.SubmitRatingOnComplete = function (scriptID) {
                if (OnCompleteFunc != null) {
                    OnCompleteFunc(onCompleteArgs);
                }

                //

                _RemoveScriptTag(scriptID);

                this.SubmitRatingOnComplete = null;
            };

            var scriptID = _AddScriptTag("SubmitRating", "MadCap.WebHelp.FeedbackController.Shared.SubmitRatingOnComplete", [["TopicID", topicID],
                                                                                                                      ["Rating", rating],
                                                                                                                      ["Comment", comment]]);
        };

        this.GetTopicComments = function (topicID, userGuid, userName, OnCompleteFunc, onCompleteArgs) {
            this.GetTopicCommentsOnComplete = function (scriptID, commentsXml) {
                if (OnCompleteFunc != null) {
                    OnCompleteFunc(commentsXml, onCompleteArgs);
                }

                //

                _RemoveScriptTag(scriptID);

                this.GetTopicCommentsOnComplete = null;
            };

            var scriptID = _AddScriptTag("GetTopicComments", "MadCap.WebHelp.FeedbackController.Shared.GetTopicCommentsOnComplete", [["TopicID", topicID],
                                                                                                                              ["UserGuid", userGuid],
                                                                                                                              ["Username", userName]]);
        };

        this.GetAnonymousEnabled = function (projectID, OnCompleteFunc, onCompleteArgs) {
            this.GetAnonymousEnabledOnComplete = function (scriptID, enabled) {
                if (OnCompleteFunc != null) {
                    OnCompleteFunc(enabled, onCompleteArgs);
                }

                //

                _RemoveScriptTag(scriptID);

                this.GetAnonymousEnabledOnComplete = null;
            };

            _AddScriptTag("GetAnonymousEnabled", "MadCap.WebHelp.FeedbackController.Shared.GetAnonymousEnabledOnComplete", [["ProjectID", projectID]]);
        };

        this.StartActivateUser = function (xmlDoc, OnCompleteFunc, onCompleteArgs) {
            this.StartActivateUserOnComplete = function (scriptID, pendingGuid) {
                if (OnCompleteFunc != null) {
                    OnCompleteFunc(pendingGuid, onCompleteArgs);
                }

                //

                _RemoveScriptTag(scriptID);

                this.StartActivateUserOnComplete = null;
            };

            var usernameNode = FMCGetChildNodeByAttribute(xmlDoc.documentElement, "Name", "Username");
            var username = FMCGetAttribute(usernameNode, "Value");
            var emailAddressNode = FMCGetChildNodeByAttribute(xmlDoc.documentElement, "Name", "EmailAddress");
            var emailAddress = FMCGetAttribute(emailAddressNode, "Value");
            var firstNameNode = FMCGetChildNodeByAttribute(xmlDoc.documentElement, "Name", "FirstName");
            var firstName = FMCGetAttribute(firstNameNode, "Value");
            var lastNameNode = FMCGetChildNodeByAttribute(xmlDoc.documentElement, "Name", "LastName");
            var lastName = FMCGetAttribute(lastNameNode, "Value");
            var countryNode = FMCGetChildNodeByAttribute(xmlDoc.documentElement, "Name", "Country");
            var country = FMCGetAttribute(countryNode, "Value");
            var postalCodeNode = FMCGetChildNodeByAttribute(xmlDoc.documentElement, "Name", "PostalCode");
            var postalCode = FMCGetAttribute(postalCodeNode, "Value");
            var genderNode = FMCGetChildNodeByAttribute(xmlDoc.documentElement, "Name", "Gender");
            var gender = FMCGetAttribute(genderNode, "Value");
            var uiLanguageOrder = "";

            _AddScriptTag("StartActivateUser", "MadCap.WebHelp.FeedbackController.Shared.StartActivateUserOnComplete", [["Username", username],
                                                                                                                 ["EmailAddress", emailAddress],
                                                                                                                 ["FirstName", firstName],
                                                                                                                 ["LastName", lastName],
                                                                                                                 ["Country", country],
                                                                                                                 ["Zip", postalCode],
                                                                                                                 ["Gender", gender],
                                                                                                                 ["UILanguageOrder", uiLanguageOrder]]);
        };

        this.StartActivateUser2 = function (xmlDoc, OnCompleteFunc, onCompleteArgs, thisObj) {
            var xml = MadCap.Utilities.Xhr.GetOuterXml(xmlDoc);

            this.StartActivateUser2OnComplete = function (scriptID, pendingGuid) {
                if (OnCompleteFunc != null) {
                    if (thisObj != null)
                        OnCompleteFunc.call(thisObj, pendingGuid, onCompleteArgs);
                    else
                        OnCompleteFunc(pendingGuid, onCompleteArgs);
                }

                //

                _RemoveScriptTag(scriptID);

                this.StartActivateUser2OnComplete = null;
            }

            _AddScriptTag("StartActivateUser2", "MadCap.WebHelp.FeedbackController.Shared.StartActivateUser2OnComplete", [["Xml", xml]]);
        };

        this.UpdateUserProfile = function (guid, xmlDoc, OnCompleteFunc, onCompleteArgs, thisObj) {
            var xml = MadCap.Utilities.Xhr.GetOuterXml(xmlDoc);

            this.UpdateUserProfileOnComplete = function (scriptID, pendingGuid) {
                if (OnCompleteFunc != null) {
                    if (thisObj != null)
                        OnCompleteFunc.call(thisObj, pendingGuid, onCompleteArgs);
                    else
                        OnCompleteFunc(pendingGuid, onCompleteArgs);
                }

                //

                _RemoveScriptTag(scriptID);

                this.UpdateUserProfileOnComplete = null;
            }

            _AddScriptTag("UpdateUserProfile", "MadCap.WebHelp.FeedbackController.Shared.UpdateUserProfileOnComplete", [["Guid", guid],
                                                                                                                 ["Xml", xml]]);
        };

        this.GetUserProfile = function (guid, OnCompleteFunc, onCompleteArgs, thisObj) {
            this.GetUserProfileOnComplete = function (scriptID, userProfileXml) {
                if (OnCompleteFunc != null) {
                    if (thisObj != null)
                        OnCompleteFunc.call(thisObj, userProfileXml, onCompleteArgs);
                    else
                        OnCompleteFunc(userProfileXml, onCompleteArgs);
                }

                //

                _RemoveScriptTag(scriptID);

                this.GetUserProfileOnComplete = null;
            }

            _AddScriptTag("GetUserProfile", "MadCap.WebHelp.FeedbackController.Shared.GetUserProfileOnComplete", [["Guid", guid]]);
        };

        this.CheckUserStatus = function (pendingGuid, OnCompleteFunc, onCompleteArgs) {
            this.CheckUserStatusOnComplete = function (scriptID, status) {
                if (OnCompleteFunc != null) {
                    OnCompleteFunc(status, onCompleteArgs);
                }

                //

                _RemoveScriptTag(scriptID);

                this.CheckUserStatusOnComplete = null;
            };

            _AddScriptTag("CheckUserStatus", "MadCap.WebHelp.FeedbackController.Shared.CheckUserStatusOnComplete", [["PendingGuid", pendingGuid]]);
        };

        this.GetSynonymsFile = function (projectID, updatedSince, OnCompleteFunc, onCompleteArgs) {
            this.GetSynonymsFileOnComplete = function (scriptID, synonymsXml) {
                if (OnCompleteFunc != null) {
                    OnCompleteFunc(synonymsXml, onCompleteArgs);
                }

                //

                _RemoveScriptTag(scriptID);
            };

            _AddScriptTag("GetSynonymsFile", "MadCap.WebHelp.FeedbackController.Shared.GetSynonymsFileOnComplete", [["ProjectID", projectID],
                                                                                                             ["UpdatedSince", updatedSince]]);
        };

        this.GetVersion = function (OnCompleteFunc, onCompleteArgs, thisObj) {
            this.GetVersionOnComplete = function (scriptID, version) {
                if (version == null) {
                    _Self.Version = 1;
                }
                else {
                    if (_Self.Version == -1 && version > 4) {
                        _Self.FeedbackServer = _GetFeedbackServerUrl(_Self.Server, 'Feedback/');
                        _Self.PulseServer = _Self.Server;
                        _Self.PulseEnabled = true;
                    }
                    _Self.FeedbackActive = true;
                    _Self.Version = version;
                }

                if (OnCompleteFunc != null) {
                    if (thisObj != null)
                        OnCompleteFunc.call(thisObj, _Self.Version, onCompleteArgs);
                    else
                        OnCompleteFunc(_Self.Version, onCompleteArgs);
                }

                //

                if (scriptID != null)
                    _RemoveScriptTag(scriptID);

                this.GetVersionOnComplete = null;
            }

            if (_Self.Version == -1)
                _AddScriptTag("GetVersion", "MadCap.WebHelp.FeedbackController.Shared.GetVersionOnComplete");
            else
                this.GetVersionOnComplete(null, _Self.Version);
        };

        this.GetPulseServerActivated = function (onCompleteFunc, onCompleteArgs, thisObj) {
            this.GetPulseServerActivatedOnComplete = function (scriptID, active) {
                if (onCompleteFunc != null) {
                    if (thisObj != null)
                        onCompleteFunc.call(thisObj, active, onCompleteArgs);
                    else
                        onCompleteFunc(active, onCompleteArgs);
                }

                //

                if (scriptID != null)
                    _RemoveScriptTag(scriptID);

                this.GetPulseServerActivatedOnComplete = null;
            }

            _AddScriptTag("GetPulseServerActivated", "MadCap.WebHelp.FeedbackController.Shared.GetPulseServerActivatedOnComplete");
        };

        this.GetPulseStreamID = function (topicID, onCompleteFunc, onCompleteArgs, thisObj) {
            this.GetPulseStreamIDOnComplete = function (scriptID, streamID) {
                if (onCompleteFunc != null) {
                    if (thisObj != null)
                        onCompleteFunc.call(thisObj, streamID, onCompleteArgs);
                    else
                        onCompleteFunc(streamID, onCompleteArgs);
                }

                //

                if (scriptID != null)
                    _RemoveScriptTag(scriptID);

                this.GetPulseStreamIDOnComplete = null;
            }

            _AddScriptTag("GetPulseStreamID", "MadCap.WebHelp.FeedbackController.Shared.GetPulseStreamIDOnComplete", [["TopicID", topicID]]);
        };

        this.GetTopicPathByStreamID = function (streamID, onCompleteFunc, onCompleteArgs, thisObj) {
            this.GetTopicPathByStreamIDOnComplete = function (scriptID, topicPath) {
                if (onCompleteFunc != null) {
                    if (thisObj != null)
                        onCompleteFunc.call(thisObj, topicPath, onCompleteArgs);
                    else
                        onCompleteFunc(topicPath, onCompleteArgs);
                }

                //

                if (scriptID != null)
                    _RemoveScriptTag(scriptID);

                this.GetTopicPathByStreamIDOnComplete = null;
            }

            _AddScriptTag("GetTopicPathByStreamID", "MadCap.WebHelp.FeedbackController.Shared.GetTopicPathByStreamIDOnComplete", [["StreamID", streamID]]);
        };

        this.GetTopicPathByPageID = function (pageID, onCompleteFunc, onCompleteArgs, thisObj) {
            this.GetTopicPathByPageIDOnComplete = function (scriptID, topicPath) {
                if (onCompleteFunc != null) {
                    if (thisObj != null)
                        onCompleteFunc.call(thisObj, topicPath, onCompleteArgs);
                    else
                        onCompleteFunc(topicPath, onCompleteArgs);
                }

                //

                if (scriptID != null)
                    _RemoveScriptTag(scriptID);

                this.GetTopicPathByPageIDOnComplete = null;
            }

            _AddScriptTag("GetTopicPathByPageID", "MadCap.WebHelp.FeedbackController.Shared.GetTopicPathByPageIDOnComplete", [["PageID", pageID]]);
        };

        this.GetPulseSearchResults = function (projectID, searchQuery, pageSize, pageIndex, onCompleteFunc, onCompleteArgs, thisObj) {
            this.GetPulseSearchResultsOnComplete = function (scriptID, searchResults) {
                if (onCompleteFunc != null) {
                    if (thisObj != null)
                        onCompleteFunc.call(thisObj, searchResults, onCompleteArgs);
                    else
                        onCompleteFunc(searchResults, onCompleteArgs);
                }

                //

                if (scriptID != null)
                    _RemoveScriptTag(scriptID);

                this.GetPulseSearchResultsOnComplete = null;
            }

            _AddScriptTag("GetPulseSearchResults", "MadCap.WebHelp.FeedbackController.Shared.GetPulseSearchResultsOnComplete", [["ProjectID", projectID],
                                                                                                                                ["SearchQuery", searchQuery],
                                                                                                                                ["PageSize", pageSize],
                                                                                                                                ["PageIndex", pageIndex]]);
        };
    };

    MadCap.WebHelp.FeedbackController.Shared = null; // A global reference to the 

    //

    MadCap.CreateNamespace("Feedback");

    MadCap.Feedback.LoginDialog = function (feedbackController, mode) {
        this._FeedbackController = feedbackController;
        this._TimeoutID = -1;
        this._Mode = mode;
        this._UserGuid = null;
        this._El = null;
    };

    var LoginDialog = MadCap.Feedback.LoginDialog;

    LoginDialog.prototype._Init = function () {
        var self = this;

        this._El = $('.login-dialog');

        $(".login-dialog-buttons .submit-button").click(function (e) {
            self.Submit();
        });
        $(".login-dialog-buttons .cancel-button").click(function (e) {
            self.Hide(false);
        });

        if (this._Mode == "edit") {
            this._UserGuid = this._FeedbackController.GetUserGuid();

            this._FeedbackController.GetUserProfile(this._UserGuid, function (userProfileXml, args) {
                var xmlDoc = MadCap.Utilities.Xhr.LoadXmlString(userProfileXml);

                $(xmlDoc.documentElement).children("Item").each(function (index, el) {
                    var $this = $(this);
                    var name = $this.attr("Name");
                    var value = $this.attr("Value");
                    var $input = $(".login-dialog input[name='" + name + "']");

                    if ($input.attr("type") == "checkbox") {
                        var boolVal = MadCap.String.ToBool(value, false);
                        $input.prop("checked", boolVal);
                    }
                    else {
                        $input.val(value);
                    }
                });
            }, null, this);
        }
        else if (this._Mode == "pulse") {
            var $pulseLoginFrame = $('#pulse-login-frame');

            if ($pulseLoginFrame.length == 0) {
                self._El.addClass('pulse');

                self._El.empty();
                self._El.append('<iframe id="pulse-login-frame" name="pulse-login-html5" style="visibility:hidden;" onload="this.style.visibility=\'visible\';"></iframe>');
                self._El.append('<button class="close-dialog"></button>');

                $('.close-dialog', self._El).click(function (e) {
                    self.Hide(true);
                });

                $('#pulse-login-frame').attr('src', self._FeedbackController.PulseServer + 'Login');
            }
        }
    };

    LoginDialog.prototype._Cleanup = function () {
        $(".login-dialog-buttons .submit-button").off("click");
        $(".login-dialog-buttons .cancel-button").off("click");

        $(".submit-button").attr("disabled", null);
        $(".status-message-box").hide();
        $(".profile-item-wrapper.error").removeClass("error");

        window.clearTimeout(this._TimeoutID);
    };

    LoginDialog.prototype.Show = function () {
        this._Init();

        var bgTintEl = MadCap.TopicHelpers.AddBackgroundTint("light");

        $(bgTintEl).animate(
        {
            opacity: 0.5
        }, 200);

        this._El.fadeIn(200);
    };

    LoginDialog.prototype.Hide = function (shouldAnimate) {
        this._Cleanup();

        MadCap.TopicHelpers.RemoveBackgroundTint();

        if (shouldAnimate)
            this._El.fadeOut();
        else
            this._El.hide();

        $(this).trigger("closed");
    };

    LoginDialog.prototype.Submit = function () {
        $(".status-message-box").hide();
        $(".profile-item-wrapper.error").removeClass("error");

        if (this._CheckErrors()) {
            this._SetStatusMessage("required-fields-missing-message", "error");

            return;
        }

        var xmlDoc = this._LoginItemsToXml();
        var self = this;

        if (this._Mode == "new") {
            this._FeedbackController.StartActivateUser2(xmlDoc, function (pendingGuid) {
                self._CheckUserStatus(pendingGuid);
            });

            this._SetStatusMessage("verification-email-sent-message");
        }
        else if (this._Mode == "edit") {
            this._FeedbackController.UpdateUserProfile(this._UserGuid, xmlDoc, function (result) {
                if (result == "00000000-0000-0000-0000-000000000000") {
                    self.Hide(true);
                }
                else {
                    self._CheckUserStatus(result);

                    self._SetStatusMessage("verification-email-sent-message");
                }
            });
        }

        $(".submit-button").attr("disabled", "disabled");
    };

    LoginDialog.prototype._CheckUserStatus = function (pendingGuid) {
        var self = this;

        this._FeedbackController.CheckUserStatus(pendingGuid, function (status) {
            if (status == "Pending") {
                self._TimeoutID = setTimeout(function () { self._CheckUserStatus(pendingGuid); }, 5000);
            }
            else {
                MadCap.Utilities.Store.setItem("LiveHelpUserGuid", status);

                self.Hide(true);
            }
        });
    };

    LoginDialog.prototype._CheckErrors = function () {
        var wereErrors = false;
        var $inputs = $(".login-dialog .profile-item-wrapper input, .login-dialog .profile-item-wrapper select");

        for (var i = 0, length = $inputs.length; i < length; i++) {
            var input = $inputs[i];
            var $input = $(input);
            var value = $input.val();
            var required = MadCap.String.ToBool(MadCap.Dom.Dataset(input, "required"), false);

            if (required && MadCap.String.IsNullOrEmpty(value)) {
                $input.closest(".profile-item-wrapper").addClass("error");

                wereErrors = true;
            }
        }

        return wereErrors;
    };

    LoginDialog.prototype._LoginItemsToXml = function () {
        var xmlDoc = MadCap.Utilities.Xhr.CreateXmlDocument("FeedbackUserProfile");
        var root = xmlDoc.documentElement;
        var $inputs = $(".login-dialog .profile-item-wrapper input");

        for (var i = 0, length = $inputs.length; i < length; i++) {
            var input = $inputs[i];
            var $input = $(input);
            var name = $input.attr("name");
            var type = $input.attr("type");
            var value = type == "checkbox" ? input.checked : $input.val();
            var item = xmlDoc.createElement("Item");

            item.setAttribute("Name", name);
            item.setAttribute("Value", value.toString());

            root.appendChild(item);
        }

        return xmlDoc;
    };

    LoginDialog.prototype._SetStatusMessage = function (messageClassName, type) {
        var $statusBox = $(".status-message-box");

        if (type == "error")
            $statusBox.addClass("error");
        else
            $statusBox.removeClass("error");

        $(".message").hide();
        $("." + messageClassName).show();

        $statusBox.fadeIn();
    };

    //
    //    Class FeedbackException
    //

    MadCap.FeedbackException = function (number, message, data) {
        MadCap.Exception.call(this, number, message);

        // Public properties

        this.Data = data;
    };

    MadCap.FeedbackException.prototype = new MadCap.Exception();
    MadCap.FeedbackException.prototype.constructor = MadCap.FeedbackException;
    MadCap.FeedbackException.prototype.base = MadCap.Exception.prototype;

    //
    //    End class FeedbackException
    //
})();
