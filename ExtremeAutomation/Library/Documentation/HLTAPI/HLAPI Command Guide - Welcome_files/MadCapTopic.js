/// <reference path="../../Scripts/jquery.js" />
/// <reference path="../../Scripts/MadCapGlobal.js" />
/// <reference path="../../Scripts/MadCapUtilities.js" />
/// <reference path="../../Scripts/MadCapDom.js" />
/// <reference path="../../Scripts/MadCapXhr.js" />
/// <reference path="../../Scripts/MadCapFeedback.js" />
/// <reference path="../Scripts/MadCapHelpSystem.js" />

/*!
* Copyright MadCap Software
* http://www.madcapsoftware.com/
*
* v9.0.0.0
*/

(function () {
    if (MadCap.Dom.Dataset(document.documentElement, "mcRuntimeFileType") != "Topic")
        return;

    MadCap.CreateNamespace("TopicHelpers");

    var TopicHelpers = MadCap.TopicHelpers;

    // Statics

    TopicHelpers.Expand = function (el) {
        var control = new TopicHelpers.ExpandingControl(el.parentNode);

        control.Toggle();
    };

    TopicHelpers.DropDown = function (el) {
        var control = new TopicHelpers.DropDownControl(el.parentNode.parentNode);

        control.Toggle();
    };

    TopicHelpers.Toggle = function (el) {
        var control = new TopicHelpers.TogglerControl(el);

        control.Toggle();
    };

    TopicHelpers.ThumbPopup_Click = function (e) {
        var popupEl = TopicHelpers.ShowThumbnailPopup(this, "click");

        if (e.preventDefault)
            e.preventDefault(); // prevents link from navigating
    };

    TopicHelpers.ThumbPopup_Hover = function (e) {
        var popupEl = TopicHelpers.ShowThumbnailPopup(this, "mouseleave");
    };

    TopicHelpers.ShowThumbnailPopup = function (aEl, showType) {
        var CONTAINER_MARGIN = 10;
        var CONTAINER_BORDER_WIDTH = 1;
        var IMAGE_PADDING = 10;
        var thumbEl = $(aEl).children("img")[0];
        var fullImageWidth = parseInt(MadCap.Dom.Dataset(thumbEl, "mcWidth"));
        var fullImageHeight = parseInt(MadCap.Dom.Dataset(thumbEl, "mcHeight"));
        var hwRatio = fullImageHeight / fullImageWidth;
        var maxWidth = document.documentElement.clientWidth - ((CONTAINER_MARGIN + CONTAINER_BORDER_WIDTH + IMAGE_PADDING) * 2);
        var maxHeight = document.documentElement.clientHeight - ((CONTAINER_MARGIN + CONTAINER_BORDER_WIDTH + IMAGE_PADDING) * 2);

        if (fullImageHeight > maxHeight) {
            fullImageHeight = maxHeight;
            fullImageWidth = fullImageHeight / hwRatio;
        }

        if (fullImageWidth > maxWidth) {
            fullImageWidth = maxWidth;
            fullImageHeight = fullImageWidth * hwRatio;
        }

        //

        var fullImageSrc = MadCap.Dom.GetAttribute(aEl, "href");
        var containerHeight = fullImageHeight + ((CONTAINER_BORDER_WIDTH + IMAGE_PADDING) * 2);
        var containerWidth = fullImageWidth + ((CONTAINER_BORDER_WIDTH + IMAGE_PADDING) * 2);
        var containerTop = (thumbEl.offsetTop + (thumbEl.offsetHeight / 2)) - (containerHeight / 2);
        var containerLeft = (thumbEl.offsetLeft + (thumbEl.offsetWidth / 2)) - (containerWidth / 2);

        // Keep within viewable area

        var scrollPosition = MadCap.Dom.GetScrollPosition();
        var clientTop = scrollPosition.Y;
        var clientBottom = clientTop + document.documentElement.clientHeight;
        var clientLeft = scrollPosition.X;
        var clientRight = clientLeft + document.documentElement.clientWidth;
        var minTop = clientTop + CONTAINER_MARGIN;
        var minLeft = clientLeft + CONTAINER_MARGIN;
        var maxBottom = clientBottom - CONTAINER_MARGIN;
        var maxRight = clientRight - CONTAINER_MARGIN;

        if (containerTop < minTop)
            containerTop = minTop;

        if (containerLeft < minLeft)
            containerLeft = minLeft;

        if (containerTop + containerHeight > maxBottom)
            containerTop = maxBottom - containerHeight;

        if (containerLeft + containerWidth > maxRight)
            containerLeft = maxRight - containerWidth;

        //

        var $containerEl = $("<div></div>");
        $containerEl.addClass("MCPopupContainer");

        var fullImageEl = document.createElement("img");
        $(fullImageEl).addClass("MCPopupFullImage");
        fullImageEl.setAttribute("src", fullImageSrc);

        $containerEl.bind(showType, function () {
            MadCap.DEBUG.Log.AddLine(showType);
            $containerEl.animate(
            {
                top: topStart,
                left: leftStart
            }, 200, function () {
                $containerEl.remove();
            });

            $(fullImageEl).animate(
            {
                width: thumbEl.offsetWidth,
                height: thumbEl.offsetHeight
            }, 200);

            $(bgTintEl).animate(
            {
                opacity: 0
            }, 200, function () { TopicHelpers.RemoveBackgroundTint(); });
        });

        $containerEl.append(fullImageEl);
        document.body.appendChild($containerEl[0]);

        // Animate it

        var topStart = thumbEl.offsetTop - (CONTAINER_BORDER_WIDTH + IMAGE_PADDING);
        var leftStart = thumbEl.offsetLeft - (CONTAINER_BORDER_WIDTH + IMAGE_PADDING);

        $containerEl.css({ top: topStart, left: leftStart }).animate(
        {
            top: containerTop,
            left: containerLeft
        }, 200);

        $(fullImageEl).css({ width: thumbEl.offsetWidth, height: thumbEl.offsetHeight }).animate(
        {
            width: fullImageWidth,
            height: fullImageHeight
        }, 200);

        // Add the background tint and animate it

        var bgTintEl = TopicHelpers.AddBackgroundTint();

        $(bgTintEl).animate(
        {
            opacity: 0.5
        }, 200);
    };

    TopicHelpers.HelpControl_Click = function (e) {
        var aEl = this;

        TopicHelpers.GetHelpControlLinks(this, function (topics) {
            // Make the links relative to the current topic
            var url = new MadCap.Utilities.Url(document.location.href);

            for (var i = topics.length - 1; i >= 0; i--) {
                var currTopic = topics[i];
                var link = new MadCap.Utilities.Url(currTopic.Link);

                if (link.FullPath == url.FullPath)
                    topics.Remove(i);

                link = link.ToRelative(url);

                currTopic.Link = link.FullPath;
            }

            // Sort them by title
            if (!$(aEl).hasClass("MCHelpControl-Related")) {
                topics.sort(function (a, b) {
                    return a.Title.localeCompare(b.Title);
                });
            }

            // Remove duplicates
            var map = new MadCap.Utilities.Dictionary();

            for (var i = topics.length - 1; i >= 0; i--) {
                var currTopic = topics[i];
                var link = currTopic.Link;

                if (map.GetItem(link)) {
                    topics.Remove(i);
                    continue;
                }

                map.Add(currTopic.Link, true);
            }

            // Move this call to the CreateLinkListPopup function
            //TopicHelpers.RemoveLinkListPopups();

            // Create the list
            var listContainerEl = TopicHelpers.CreateLinkListPopup(topics, document.body, e.pageY, e.pageX, aEl);
        }, null);

        e.preventDefault();
        e.stopPropagation();
    };

    TopicHelpers.GetHelpControlLinks = function (node, callbackFunc) {
        var links = new Array();
        var $node = $(node);

        if (!_HelpSystem.InPreviewMode) {
            if (IsEmbeddedTopic()) {
                //                if (_HelpSystem.IsMerged()) {
                var indexKeywords = $node.attr("data-mc-keywords");

                if (indexKeywords != null) {
                    if (indexKeywords == "")
                        callbackFunc(links);

                    var keywords = indexKeywords.split(";");

                    MadCap.Utilities.AsyncForeach(keywords, function (keyword, callback) {
                        _HelpSystem.FindIndexEntry(keyword, function (rootEntry, entry) {
                            if (entry != null && entry.linkList) {
                                links = links.concat(entry.linkList);
                            }

                            callback();
                        });
                    },
                        function () {
                            callbackFunc(_HelpSystem.SortLinkList(links));
                        });


                    //_HelpSystem.GetIndex(function (xmlDoc) {

                    //    for (var i = 0; i < keywords.length; i++) {
                    //        keywords[i] = keywords[i].replace("%%%%%", ";");

                    //        var currKeyword = keywords[i].replace("\\:", "%%%%%");
                    //        var keywordPath = currKeyword.split(":");
                    //        var level = keywordPath.length - 1;
                    //        var indexKey = level + "_" + keywordPath[level].replace("%%%%%", ":");

                    //        var currLinkMap = _HelpSystem.GetIndexLinks(indexKey);

                    //        // currLinkMap may be blank if keywords[i] isn't found in index XML file (user may have deleted keyword after associating it with a K-Link)

                    //        if (currLinkMap) {
                    //            currLinkMap.ForEach(function (key, value) {
                    //                linkMap[linkMap.length] = { Title: key, Link: value };
                    //            });
                    //        }
                    //    }

                    //    callbackFunc(linkMap);
                    //}, null);

                    return;
                }
                else {
                    var concepts = $node.attr("data-mc-concepts");

                    if (concepts != null) {
                        _HelpSystem.GetConceptsLinks(concepts, callbackFunc);

                        return;
                    }
                }
                //                }
            }
        }

        var topics = $node.attr("data-mc-topics");

        if (topics != null) {
            topicPairs = topics.split("||");

            if (topicPairs == "") {
                callbackFunc(links);
            }

            for (var i = 0, length = topicPairs.length; i < length; i++) {
                var topicAndPath = topicPairs[i].split("|");

                links[links.length] = { Title: topicAndPath[0], Link: topicAndPath[1] };
            }
        }

        callbackFunc(links);
    };

    TopicHelpers.Hyperlink_Onclick = function (e) {
        var $this = $(this);

        if ($this.hasClass("MCTopicPopup") || $this.hasClass("MCPopupThumbnailLink") || $this.hasClass("MCHelpControl") || $this.hasClass("reply-comment-button"))
            return;

        var href = MadCap.Dom.GetAttribute(this, "href");

        if (MadCap.String.StartsWith(href, "http:") || MadCap.String.StartsWith(href, "https:"))
            return;

        var target = MadCap.Dom.GetAttribute(this, "target");

        if (target != null)
            return;

        if (IsEmbeddedTopic()) {
            var url = new MadCap.Utilities.Url(document.location.href);

            if (MadCap.String.StartsWith(href, '#')) {
                url = new MadCap.Utilities.Url(url.PlainPath + href);
            }
            else {
                url = url.ToFolder().CombinePath(href);
            }

            MadCap.Utilities.CrossFrame.PostMessageRequest(parent, "navigate-topic", [url.FullPath], null);

            e.preventDefault(); // prevents link from navigating
        }
    };

    TopicHelpers.ScrollToBookmark = function (id) {
        var $target = $("#" + id);
        if ($target.length == 0)
            $target = $("[name = '" + id + "']");

        if ($target.length > 0) {
            if (Unhide($target[0])) {
                var targetOffsetTop = $target.offset().top;

                $("html, body").animate({ scrollTop: targetOffsetTop });
            }
        }
    };

    //

    $(WindowOnload);
    $(window).hashchange(Window_Onhashchange); // hashchange polyfill

    function WindowOnload(e) {
        // Apply placeholder polyfill
        $("input, textarea").placeholder();

        //

        if (document.location.hash.length > 0) {
            var href = new MadCap.Utilities.Url(document.location.hash.substring(1));
            ProcessBookmark(href.ToNoQuery().FullPath);
        }

        // if embedded topic or topic popup, hide any MCWebHelpFramesetLinks
        if (IsEmbeddedTopic() || IsTopicPopup()) {
            $(".MCWebHelpFramesetLink").hide();
        }

        // Handle clicks to anchors using event delegation. This way, anchors added dynamically (via help controls, etc.) will be handled without needing to attach the handler then.
        $(document).on("click", "a, area", MadCap.TopicHelpers.Hyperlink_Onclick);

        // Set up thumbnail popups and hovers
        $(".MCPopupThumbnailPopup").click(MadCap.TopicHelpers.ThumbPopup_Click);
        $(".MCPopupThumbnailHover").mouseover(MadCap.TopicHelpers.ThumbPopup_Hover);

        var helpControls = $("a.MCHelpControl").click(MadCap.TopicHelpers.HelpControl_Click);

        // Set up buttons
        $(".print-button").click(function (e) {
            window.print();
        });

        $(".expand-all-button").click(function (e) {
            var $this = $(this);

            if ($this.hasClass("expand-all-button"))
                TopicHelpers.TextEffectControl.ExpandAll("open");
            else if ($this.hasClass("collapse-all-button"))
                TopicHelpers.TextEffectControl.ExpandAll("close");

            ToggleButtonState(this);
        });
        $(".remove-highlight-button").click(function (e) {
            RemoveHighlight();
        });

        $(".previous-topic-button").click(function (e) {
            MadCap.Utilities.CrossFrame.PostMessageRequest(parent, "navigate-previous");
        });

        $(".next-topic-button").click(function (e) {
            MadCap.Utilities.CrossFrame.PostMessageRequest(parent, "navigate-next");
        });

        //

        if (MadCap.String.Contains(navigator.userAgent, "iphone", false)) {
            window.scrollTo(0, 1);
        }

        // iPad scrolling issue with iframe. The iframe contents that aren't visible don't render after scrolling.
        // http://stackoverflow.com/questions/10805301/how-can-i-scroll-an-iframe-in-ios-4-with-2-fingers/10807318#10807318
        if (MadCap.IsIOS()) {
            // Can't use jQuery here because append() will cause any inline <script> to be executed again.
            //var $wrapperDiv = $("<div id='ios-wrapper'></div>");
            //$wrapperDiv.append($(document.body).children()).appendTo(document.body);
            var $wrapperDiv = $("<div id='ios-wrapper'></div>").appendTo(document.body);
            var wrapperDiv = $wrapperDiv[0];

            for (var i = document.body.childNodes.length - 2; i >= 0; i--) {
                var child = document.body.childNodes[i];

                wrapperDiv.insertBefore(child, wrapperDiv.firstChild);
            }
        }

        //

        //                var searchQuery = path.indexOf('?');
        //		if(searchQuery > 0) {
        //        {
        //			// This means we've got searchQuery info within the URL, so we'll do some highlighting
        //            runHighlighter(searchQuery);
        //		}

        HighlightSearchTerms();

        //

        var homeFrame = parent;

        if (IsTopicPopup()) {
            homeFrame = parent.parent;
        }

        var pathToHelpSystem = $(document.documentElement).attr('data-mc-path-to-help-system');
        var url = new MadCap.Utilities.Url(document.location.href).CombinePath(pathToHelpSystem).ToFolder().CombinePath('Data/HelpSystem.xml');

        _HelpSystem = new MadCap.WebHelp.HelpSystem(null, null, url.FullPath, null, null);
        _HelpSystem.Load(function () {
            UpdateCurrentTopicIndex();

            if (_HelpSystem.LiveHelpEnabled) {
                _FeedbackController = new MadCap.WebHelp.FeedbackController(_HelpSystem.LiveHelpServer);
                _FeedbackController.Init(function () {
                    if (_FeedbackController.FeedbackActive) {
                        // Request the CSHID from the parent frame
                        MadCap.Utilities.CrossFrame.PostMessageRequest(parent, "get-csh-id", null, function (data) {
                            var cshid = data != null ? data[0] : null;

                            if (_TopicID != null) {
                                // Log the topic view
                                _FeedbackController.LogTopic(_TopicID, cshid, function () {
                                    var $feedbackWrapper = $(".feedback-comments-wrapper");

                                    if (!IsTopicPopup()) {
                                        if (!_FeedbackController.PulseEnabled) { // using Feedback Server
                                            $feedbackWrapper.removeClass("hidden");

                                            _CommentLengthExceededMessage = $("#new-comment-form").attr("data-comment-length-exceeded-message")
                                                || "The maximum comment length was exceeded by {n} characters.";

                                            // If anonymous comments are enabled, the username field will be displayed.
                                            _FeedbackController.GetAnonymousEnabled(_HelpSystem.LiveHelpOutputId, function (anonEnabled) {
                                                _AnonymousCommentsEnabled = anonEnabled;

                                                if (anonEnabled)
                                                    $(document.documentElement).addClass("feedback-anonymous-enabled");
                                            });

                                            var username = MadCap.Utilities.Store.getItem("LiveHelpUsername");
                                            $(".username").val(username);

                                            // Hook up the comment submit button handler
                                            $(".comment-submit").click(CommentSubmit_Click);

                                            // Hook up the reply comment button handler (using event delegation)
                                            $(".feedback-comments-wrapper .comments").on("click", ".reply-comment-button", ReplyComment_Click);

                                            // Get topic comments
                                            RefreshComments();
                                        }
                                        else if (_FeedbackController.PulseActive) {
                                            _FeedbackController.GetPulseStreamID(_TopicID, function (streamID) {
                                                $feedbackWrapper.empty();

                                                var src = _FeedbackController.PulseServer + "streams/" + streamID + "/activities?frame=stream";
                                                var $pulseIframe = $("<iframe name='topiccomments-html5' class='pulse-frame' title='Topic Comments' frameborder='0'></iframe>");
                                                $pulseIframe.appendTo($feedbackWrapper);
                                                $pulseIframe.css("height", "1000px"); // -TODO- Fix this
                                                if (!($.browser.msie && parseInt($.browser.version, 10) === 7)) // if not ie7
                                                {
                                                    $pulseIframe.css("visibility", "hidden");
                                                    $pulseIframe.attr("onload", "this.style.visibility='visible';");
                                                }
                                                $pulseIframe.attr("src", src);

                                                $feedbackWrapper.removeClass("hidden");
                                            });
                                        }
                                    }
                                });
                            }
                        });
                    }
                });
            }
        });
    }

    function Window_Onhashchange(e) {
        var url = new MadCap.Utilities.Url(document.location.href);

        if (!MadCap.String.IsNullOrEmpty(url.Fragment)) {
            var id = url.Fragment.substring(1);

            TopicHelpers.ScrollToBookmark(id);
        }
    }

    function ProcessBookmark(bookmarkName) {
        var el = $("[name='" + bookmarkName + "']");

        if (el.length > 0)
            Unhide(el[0]);
    }

    function IsEmbeddedTopic() {
        return window.name == "topic";
    }

    function IsTopicPopup() {
        return window.name == "MCPopup";
    }

    function ToggleButtonState(buttonEl) {
        var $buttonEl = $(buttonEl);
        var state1 = $buttonEl.attr("data-state1-class");
        var state2 = $buttonEl.attr("data-state2-class");
        var currState = $buttonEl.attr("data-current-state") || "1";
        var nextState = currState == "1" ? "2" : "1";

        $buttonEl.attr("data-current-state", nextState);
        $buttonEl.toggleClass(state1).toggleClass(state2);
        $buttonEl.attr("title", $buttonEl.attr("data-state" + nextState + "-title"));
    }

    function UpdateCurrentTopicIndex() {
        MadCap.Utilities.CrossFrame.PostMessageRequest(parent, "get-href", null, function (data) {
            if (data) {
                var url = new MadCap.Utilities.Url(unescape(data[0]));

                var href = new MadCap.Utilities.Url(url.Fragment.substring(1));
                var bsPath = url.QueryMap.GetItem('BrowseSequencesPath');

                _HelpSystem.SetBrowseSequencePath(bsPath, href);
            }
        });
    }

    function CommentSubmit_Click(e) {
        var $form = $(this).closest(".comment-form-wrapper");
        var userGuid = null;
        var username = $form.children(".username-field").val();
        var subject = $form.children(".subject-field").val();
        var comment = $form.find(".body-field").val();
        var parentCommentID = null;
        var $formParent = $form.parent();

        if ($formParent.hasClass("comment"))
            parentCommentID = $formParent.attr("data-mc-comment-id");

        AddComment(username, subject, comment, parentCommentID);
    }

    function AddComment(username, subject, comment, parentCommentID) {
        if (_AnonymousCommentsEnabled) {
            MadCap.Utilities.Store.setItem("LiveHelpUsername", username);

            try {
                _FeedbackController.AddComment(_TopicID, null, username, subject, comment, parentCommentID, RefreshComments);
            }
            catch (ex) {
                var message = _CommentLengthExceededMessage.replace(/{n}/g, ex.Data.ExceedAmount);
                alert(message);
            }
        }
        else {
            MadCap.Utilities.CrossFrame.PostMessageRequest(parent, "login-user", null, function (data) {
                var userGuid = data[0];

                if (userGuid != null) {
                    try {
                        _FeedbackController.AddComment(_TopicID, userGuid, username, subject, comment, parentCommentID, RefreshComments);
                    }
                    catch (ex) {
                        var message = _CommentLengthExceededMessage.replace(/{n}/g, ex.Data.ExceedAmount);
                        alert(message);
                    }
                }
            });
        }
    }

    function ReplyComment_Click(e) {
        e.preventDefault();

        var $formParent = $(this).closest(".comment");

        if ($formParent.children(".comment-form-wrapper")[0] != null)
            return;

        // create a copy of the new comment form and append it to the end of the current comment

        var $newForm = $("#new-comment-form").clone();
        $newForm.attr("id", null);
        $newForm.children(".comment-submit").click(CommentSubmit_Click);
        $formParent.children(".buttons").after($newForm);
        $newForm.hide().slideDown();
    }

    function RefreshComments() {
        MadCap.Utilities.CrossFrame.PostMessageRequest(parent, "get-user-guid", null, function (data) {
            var userGuid = data[0];

            _FeedbackController.GetTopicComments(_TopicID, userGuid, null, function (commentsXml) {
                var xmlDoc = MadCap.Utilities.Xhr.LoadXmlString(commentsXml);
                var $comments = $(".comments");
                $comments.children().not(".mc-template").remove();

                BuildComments(xmlDoc.documentElement, $comments);
            });
        });
    }

    function BuildComments(xmlNode, htmlContainerNode) {
        var $xmlCommentNodes = $(xmlNode).children("Comment");
        var $commentTemplate = $(".comments .comment.mc-template");

        for (var i = 0, length = $xmlCommentNodes.length; i < length; i++) {
            var $xmlCommentNode = $($xmlCommentNodes[i]);
            var xmlUsername = $xmlCommentNode.attr("User");
            var xmlTimestamp = $xmlCommentNode.attr("DateUTC") || $xmlCommentNode.attr("Date"); // Feedback V1 used "Date", V2 uses "DateUTC". We could do a version check, but simply checking for the attribute is easier.
            var xmlSubject = $xmlCommentNode.attr("Subject");
            var xmlCommentID = $xmlCommentNode.attr("CommentID");
            var xmlBody = $xmlCommentNode.children("Body").text();

            var $commentNode = $commentTemplate.clone();
            $commentNode.removeClass("mc-template");

            $commentNode.attr("data-mc-comment-id", xmlCommentID);
            $(".username", $commentNode).text(xmlUsername);
            $(".timestamp", $commentNode).text(xmlTimestamp);
            $(".subject", $commentNode).text(xmlSubject);
            $(".body", $commentNode).text(xmlBody);

            $(htmlContainerNode).append($commentNode);

            BuildComments($xmlCommentNode.children("Comments")[0], $commentNode);
        }
    }

    function RemoveHighlight() {
        for (var index = 1; index <= 10; index++) {
            $('body').removeHighlight('mc-highlightSearch' + index);
        }
    }

    function HighlightSearchTerms() {
        MadCap.Utilities.CrossFrame.PostMessageRequest(parent, "get-href", null, function (data) {
            if (data) {
                var url = new MadCap.Utilities.Url(unescape(data[0]));
                var highlight = url.QueryMap.GetItem("Highlight");

                if (MadCap.String.IsNullOrEmpty(highlight)) {
                    return;
                }

                var terms = highlight.split(" ");
                for (var index = 0; index < terms.length; index++) {
                    $('body').highlight(terms[index], 'mc-highlightSearch' + (index + 1));
                }
            }
        });
    }

    function Highlight(term, color, caseSensitive, searchType) {
        if (term == "") {
            return;
        }

        ApplyHighlight(document.body, term, color, caseSensitive, searchType);

        // Scroll to first highlighted term

        if (_FirstHighlight && _FirstHighlight.offsetTop > document.documentElement.clientHeight) {
            document.documentElement.scrollTop = _FirstHighlight.offsetTop;
        }
    }

    function MergeTextNodes(node) {
        for (var i = node.childNodes.length - 1; i >= 1; i--) {
            var currNode = node.childNodes[i];
            var prevNode = currNode.previousSibling;

            if (currNode.nodeType == 3 && prevNode.nodeType == 3) {
                prevNode.nodeValue = prevNode.nodeValue + currNode.nodeValue;
                node.removeChild(currNode);
            }
        }

        for (var i = 0; i < node.childNodes.length; i++) {
            MergeTextNodes(node.childNodes[i]);
        }
    }

    function ApplyHighlight(root, term, color, caseSensitive, searchType) {
        var re = null;

        if (searchType == "NGram") {
            re = new RegExp(term, "g" + (caseSensitive ? "" : "i"));
        }
        else {
            var escTerm = term.replace(/([*^$+?.()[\]{}|\\])/g, "\\$1"); // Escape regex

            re = new RegExp("(^|\\s|[.,;!#$/:?'\"()[\\]{}|=+*_\\-\\\\])" + escTerm + "($|\\s|[.,;!#$/:?'\"()[\\]{}|=+*_\\-\\\\])", "g" + (caseSensitive ? "" : "i"));
        }

        for (var i = root.childNodes.length - 1; i >= 0; i--) {
            var node = root.childNodes[i];

            ApplyHighlight(node, term, color, caseSensitive, searchType);

            if (node.nodeType != 3 || node.parentNode.nodeName == "SCRIPT") {
                continue;
            }

            var currNode = node;
            var text = currNode.nodeValue;

            for (var match = re.exec(text); match != null; match = re.exec(text)) {
                var pos = match.index + (searchType == "NGram" ? 0 : match[1].length);
                var posEnd = pos + term.length;
                var span = document.createElement("span");

                span.className = "highlight";
                span.style.fontWeight = "bold";
                span.style.backgroundColor = color.split(",")[0];
                span.style.color = color.split(",")[1];

                var span2 = document.createElement("span");

                span2.className = "SearchHighlight" + (_ColorIndex + 1);
                span2.appendChild(document.createTextNode(text.substring(pos, posEnd)));

                span.appendChild(span2);

                currNode.nodeValue = text.substring(0, pos);
                currNode.parentNode.insertBefore(span, currNode.nextSibling);
                currNode.parentNode.insertBefore(document.createTextNode(text.substring(posEnd, text.length)), span.nextSibling);

                currNode = currNode.nextSibling.nextSibling;
                text = currNode.nodeValue;

                //

                if (_FirstHighlight == null || span.offsetTop < _FirstHighlight.offsetTop) {
                    _FirstHighlight = span;
                }

                //

                Unhide(span);
            }
        }
    }

    function Unhide(el) {
        var didOpen = false;

        for (var currNode = el.parentNode; currNode.nodeName != "BODY"; currNode = currNode.parentNode) {
            var $currNode = $(currNode);

            if ($currNode.hasClass("MCExpanding")) {
                var control = TopicHelpers.TextEffectControl.FindControl($currNode[0]);
                if (control == null) {
                    control = new MadCap.TopicHelpers.ExpandingControl(currNode);
                }
                control.Open();
                didOpen = true;
            }
            else if ($currNode.hasClass("MCDropDown")) {
                var control = TopicHelpers.TextEffectControl.FindControl($currNode[0]);
                if (control == null) {
                    control = new MadCap.TopicHelpers.DropDownControl(currNode);
                }
                control.Open();
                didOpen = true;
            }
            else {
                var targetName = $(currNode).attr("data-mc-target-name");

                if (targetName != null) {
                    var togglerNodes = MadCap.Dom.GetElementsByClassName("MCToggler", null, document.body);

                    for (var i = 0, length = togglerNodes.length; i < length; i++) {
                        var targets = $(togglerNodes[i]).attr("data-mc-targets").split(";");
                        var found = false;

                        for (var j = 0; j < targets.length; j++) {
                            if (targets[j] == targetName) {
                                found = true;

                                break;
                            }
                        }

                        if (!found)
                            continue;

                        var control = TopicHelpers.TextEffectControl.FindControl(togglerNodes[i]);
                        if (control == null) {
                            control = new MadCap.TopicHelpers.TogglerControl(togglerNodes[i]);
                        }
                        control.Open();
                        didOpen = true;

                        break;
                    }
                }
            }
        }

        return didOpen;
    }

    MadCap.Utilities.CrossFrame.AddMessageHandler(function (message, dataValues, responseData) {
        var returnData = { Handled: false, FireResponse: true };

        if (message == "print") {
            window.focus();
            window.print();

            returnData.Handled = true;
        }
        else if (message == "expand-all") {
            TopicHelpers.TextEffectControl.ExpandAll("open");

            returnData.Handled = true;
        }
        else if (message == "collapse-all") {
            TopicHelpers.TextEffectControl.ExpandAll("close");

            returnData.Handled = true;
        }
        else if (message == "get-topic-id") {
            responseData[responseData.length] = _TopicID;

            returnData.Handled = true;
        }
        else if (message == "get-topic-url") {
            responseData[responseData.length] = document.location.href;

            returnData.Handled = true;
        }
        else if (message == "remove-highlight") {
            RemoveHighlight();
            returnData.Handled = true;
        }
        else if (message == "get-bs-path") {
            var url = new MadCap.Utilities.Url(document.location.href);
            var bsPath = url.QueryMap.GetItem("BrowseSequencePath");

            if (bsPath == null)
                bsPath = MadCap.Dom.Dataset(document.documentElement, "mcBrowseSequencePath");

            responseData[responseData.length] = bsPath;
            responseData[responseData.length] = url.FullPath;

            //

            returnData.Handled = true;
        }
        else if (message == "reload-pulse") {
            MadCap.Utilities.CrossFrame.PostMessageRequest(frames["topiccomments-html5"], "reload");

            //

            returnData.Handled = true;
        }
        else if (message == "logout-complete") {
            MadCap.Utilities.CrossFrame.PostMessageRequest(parent, "logout-complete");

            returnData.Handled = true;
        }
        else if (message == "set-pulse-login-id") {
            if (_FeedbackController != null)
                _FeedbackController.PulseUserGuid = dataValues[0];

            MadCap.Utilities.CrossFrame.PostMessageRequest(parent, "set-pulse-login-id", dataValues);

            returnData.Handled = true;
        }

        return returnData;
    }, null);

    var _ColorTable = new Array("#ffff66,#000000",
								"#a0ffff,#000000",
								"#99ff99,#000000",
								"#ff9999,#000000",
								"#ff66ff,#000000",
								"#880000,#ffffff",
								"#00aa00,#ffffff",
								"#886800,#ffffff",
								"#004699,#ffffff",
								"#990099,#ffffff");
    var _ColorIndex = 0;
    var _FirstHighlight = null;
    var _HelpSystem = null;
    var _FeedbackController = null;
    var _AnonymousCommentsEnabled = false;
    var _TopicID = MadCap.Dom.Dataset(document.documentElement, "mcLiveHelp");
    var _CommentLengthExceededMessage = null;
})();
