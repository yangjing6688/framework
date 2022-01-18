/// <reference path="../../Scripts/jquery.js" />
/// <reference path="../../Scripts/MadCapGlobal.js" />
/// <reference path="../../Scripts/MadCapUtilities.js" />
/// <reference path="../../Scripts/MadCapDom.js" />
/// <reference path="../../Scripts/MadCapFeedback.js" />
/// <reference path="MadCapToc.js" />
/// <reference path="MadCapIndex.js" />
/// <reference path="MadCapHelpSystem.js" />
/// <reference path="MadCapSearch.js" />

/*!
 * Copyright MadCap Software
 * http://www.madcapsoftware.com/
 *
 * v9.1.0.0
 */

(function () {
    if (MadCap.Dom.Dataset(document.documentElement, "mcRuntimeFileType") != "Default")
        return;

    function Window_Onload(e) {
        MadCap.DEBUG.Log.AddLine(window.name + "onload");
        MadCap.DEBUG.Log.AddLine(window.name + "hash: " + document.location.hash);
        MadCap.DEBUG.Log.AddLine(window.name + "search: " + document.location.search);

        // IE9 bug - left/right border radii are reversed in RTL elements
        if ($.browser.msie && $.browser.version <= 9.0) {
            var $searchField = $("#search-field");
            if ($searchField.css("direction") == "rtl") {
                $searchField.css({
                    "border-top-left-radius": $searchField.css("border-top-right-radius"),
                    "border-top-right-radius": $searchField.css("border-top-left-radius"),
                    "border-bottom-left-radius": $searchField.css("border-bottom-right-radius"),
                    "border-bottom-right-radius": $searchField.css("border-bottom-left-radius")
                });
            }

            var $contentBody = $("#contentBody");
            if ($contentBody.css("direction") == "rtl") {
                $contentBody.css({
                    "border-top-left-radius": $contentBody.css("border-top-right-radius"),
                    "border-top-right-radius": $contentBody.css("border-top-left-radius")
                });
            }
        }

        // Apply placeholder polyfill
        $("input, textarea").placeholder();

        // Set up navigation tabs click handlers
        $(".tabs .tabs-nav li").click(NavTabs_Click);

        // Set up search
        $(".search-submit").click(function (e) {
            SearchFormSubmit();
        });
        $("#search-field").keypress(function (e) {
            if (e.which != 13)
                return;

            SearchFormSubmit();

            e.preventDefault();
        });
        $(".search-filter").click(function (e) {
            $(this).addClass("open");

            if (window.PIE) {
                // When a filter is selected it causes the search bar width to change. PIE wasn't automatically detecting this and re-rendering as it should have been.
                // So instead, manually detach and re-attach to workaround this.
                $(".search-submit-wrapper").each(function () {
                    PIE.detach(this);
                    PIE.attach(this);
                });
            }

            var $filterContent = $(".search-filter-content", this);
            $filterContent.fadeIn(200);
            $filterContent.css("max-height", $(window).height() - $filterContent.offset().top);
        });
        var timer = null;
        $(".search-filter").mouseenter(function (e) {
            clearTimeout(timer);
        });
        $(".search-filter").mouseleave(function (e) {
            var $searchFilter = $(this);
            var $searchFilterContent = $(".search-filter-content", this);

            timer = setTimeout(function () {
                $searchFilterContent.fadeOut(200, function () {
                    $searchFilter.removeClass("open");
                });
            }, 500);
        });
        $(".search-filter-content").click(function (e) {
            var filterText = $(e.target).text();

            $(this).prev().text(filterText);

            // if the search pane is currently active, redo the search to refresh the search results with the new filter applied
            if ($("#searchPane").is(":visible")) {
                var searchQuery = $("#search-field").val();

                if (MadCap.String.IsNullOrEmpty(searchQuery))
                    return;

                DoSearch(searchQuery);
            }
        });

        // Set up the resize bar
        $("#navigationResizeBar").mousedown(NavigationResizeBar_MouseDown);
        $("#show-hide-navigation").click(ShowHideNavigation_Click);
        AdjustTabs(parseInt($("#navigation").css("width")));

        // Store the page title. Each topic title will be appended to it when they're loaded.
        var $title = $("title");
        $title.attr("data-title", document.title);

        // Set up the topic onload handler
        $("#topic").load(function () {
            // Zero out the topic rating
            SetFeedbackRating(0);

            // Add the topic title to the page title
            MadCap.Utilities.CrossFrame.PostMessageRequest(frames["topic"], "get-title", null, function (data) {
                var defaultTitle = $title.attr("data-title");
                var newTitle = defaultTitle;

                if (!MadCap.String.IsNullOrEmpty(defaultTitle))
                    newTitle += " - ";

                document.title = newTitle + data[0];
            });

            //            // Enable/disable the previous/next buttons
            //            GetAdvanceUrl("previous", function (href)
            //            {
            //                $(".previous-topic-button").attr("disabled", href == null ? "disabled" : null);
            //            });
            //            GetAdvanceUrl("next", function (href)
            //            {
            //                $(".next-topic-button").attr("disabled", href == null ? "disabled" : null);
            //            });

            // Update current topic index
            //UpdateCurrentTopicIndex();

            // Request the topic ID from the topic iframe
            MadCap.Utilities.CrossFrame.PostMessageRequest(frames["topic"], "get-topic-id", null, function (data) {
                _TopicID = data[0];

                if (_TopicID != null) {
                    // Get the topic rating
                    UpdateRating();
                }
            });
        });

        // Set up buttons
        $(".print-button").click(function (e) {
            MadCap.Utilities.CrossFrame.PostMessageRequest(frames["topic"], "print");
        });

        $(".expand-all-button").click(function (e) {
            var $this = $(this);

            if ($this.hasClass("expand-all-button"))
                MadCap.Utilities.CrossFrame.PostMessageRequest(frames["topic"], "expand-all");
            else if ($this.hasClass("collapse-all-button"))
                MadCap.Utilities.CrossFrame.PostMessageRequest(frames["topic"], "collapse-all");

            ToggleButtonState(this);
        });
        $(".remove-highlight-button").click(function (e) {
            MadCap.Utilities.CrossFrame.PostMessageRequest(frames["topic"], "remove-highlight");
        });

        $(".previous-topic-button").click(function (e) {
            //_TocPane.NavigateTopic("previous");
            PreviousTopic();
        });

        $(".next-topic-button").click(function (e) {
            //_TocPane.NavigateTopic("next");
            NextTopic();
        });

        // Load the help system
        MadCap.WebHelp.HelpSystem.LoadHelpSystem("Data/HelpSystem.xml", function (helpSystem) {
            _HelpSystem = helpSystem;

            if (_HelpSystem.LiveHelpEnabled) {
                _FeedbackController = new MadCap.WebHelp.FeedbackController(_HelpSystem.LiveHelpServer);
                _FeedbackController.Init(function () {
                    if (_FeedbackController.PulseActive) {
                        $(document.documentElement).addClass('pulse-active');
                    }

                    if (_FeedbackController.FeedbackActive) {
                        $(document.documentElement).addClass('feedback-active');

                        InitCommunityFeatures();
                    }
                });
            }

            if (!MadCap.String.IsNullOrEmpty(_HelpSystem.DefaultSkin.Tabs))
                LoadDefaultPane();

            // Load initial settings from hash
            if (document.location.hash.length > 1)
                LoadFromHash();
            else
                LoadFile(_HelpSystem.DefaultStartTopic);

            // Set the size of the browser if enabled in the skin
            SetSize(_HelpSystem.DefaultSkin);

            // Load search filters
            _HelpSystem.LoadMergedSearchFilters(function (filterMap) {
                if (filterMap == null || filterMap.GetLength() == 0) {
                    if (window.PIE) {
                        $(".search-submit-wrapper").each(function () {
                            PIE.attach(this);
                        });
                    }

                    return;
                }

                $(".search-filter-wrapper").show();

                if (window.PIE) {
                    $(".search-filter, .search-submit-wrapper").each(function () {
                        PIE.attach(this);
                    });
                }

                var filterNames = [];

                filterMap.ForEach(function (key, value) {
                    filterNames.push(key);
                    return true;
                });

                filterNames.sort();

                for (var i = 0, length = filterNames.length; i < length; i++) {
                    $(".search-filter-content ul").append($("<li></li>").text(filterNames[i]));
                }
            });
        });
    }

    function Window_Onhashchange(e) {
        MadCap.DEBUG.Log.AddLine(window.name + "onhashchange: " + document.location.hash);

        if (document.location.hash.length > 1)
            LoadFromHash();
        else
            LoadFile(_HelpSystem.DefaultStartTopic);
    }

    function InitCommunityFeatures() {
        // Set up topic rating mouse click event
        $(".star-buttons").click(FeedbackRating_Click);

        // Set the login/edit user profile button depending if the user is logged in
        UpdateLoginButton();

        $(".buttons").on("click", ".login-button", function (e) {
            _LoginDialog = new MadCap.Feedback.LoginDialog(_FeedbackController, _FeedbackController.PulseEnabled ? "pulse" : "new");

            if (!_FeedbackController.PulseEnabled) {
                $(_LoginDialog).bind("closed", function () {
                    UpdateLoginButton();
                });
            }

            _LoginDialog.Show();
        });

        $(".buttons").on("click", ".edit-user-profile-button", function (e) {
            if (_FeedbackController.PulseEnabled) {
                document.location.hash = 'pulse-#!streams/' + _FeedbackController.PulseUserGuid + '/settings';
            }
            else {
                _LoginDialog = new MadCap.Feedback.LoginDialog(_FeedbackController, "edit");

                $(_LoginDialog).bind("closed", function () {
                    UpdateLoginButton();
                });

                _LoginDialog.Show();
            }
        });
    }

    function SearchFormSubmit() {
        var searchQuery = $("#search-field").val();

        if (MadCap.String.IsNullOrEmpty(searchQuery))
            return;

        document.location.hash = "search-" + searchQuery;
    }

    function DoSearch(searchQuery, searchTopics, searchCommunity, communityPageSize, communityPageIndex) {
        var filterName = $.trim($(".search-filter span").text()); // trim this because the trailing space from below will get copied here if the "all files" filter is selected from the dropdown
        var noFilterName = $.trim($(".search-filter li").first().text()); // trim this because in IE 7 there's a trailing space after the text for some reason

        if (typeof searchTopics == "undefined")
            searchTopics = true;
        if (typeof searchCommunity == "undefined")
            searchCommunity = _HelpSystem.DisplayCommunitySearchResults;
        if (typeof communityPageSize == "undefined")
            communityPageSize = _HelpSystem.CommunitySearchResultsCount;
        if (typeof communityPageIndex == "undefined")
            communityPageIndex = 0;

        if (filterName == noFilterName)
            filterName = null;

        $("#resultList").remove();

        ShowPane("search");

        if (searchTopics) {
            Search(searchQuery, filterName, function (results) {
                if (searchCommunity) {
                    CommunitySearch(searchQuery, filterName, communityPageSize, communityPageIndex, function (communityResults) {
                        BuildSearchResults(searchQuery, results, communityResults);
                    });
                }
                else {
                    BuildSearchResults(searchQuery, results, null);
                }
            });
        }
        else if (searchCommunity) {
            CommunitySearch(searchQuery, filterName, communityPageSize, communityPageIndex, function (communityResults) {
                BuildSearchResults(searchQuery, null, communityResults);
            });
        }
    }

    function Search(searchQuery, filterName, OnCompleteFunc) {
        if (_SearchPane == null)
            _SearchPane = new MadCap.WebHelp.SearchPane(_HelpSystem);

        var $searchPane = $("#searchPane").addClass("loading");

        _SearchPane.Init(function () {
            _SearchPane.StartSearch(searchQuery, filterName, function (resultSet) {
                var results = PrepareSearchResults(resultSet);

                $searchPane.removeClass("loading");

                if (OnCompleteFunc != null)
                    OnCompleteFunc(results);
            }, null);
        });
    }

    function CommunitySearch(searchQuery, filterName, pageSize, pageIndex, OnCompleteFunc) {
        if (_SearchPane == null)
            _SearchPane = new MadCap.WebHelp.SearchPane(_HelpSystem);

        var $searchPane = $("#searchPane").addClass("loading");

        _SearchPane.Init(function () {
            _SearchPane.StartPulseSearch(searchQuery, pageSize, pageIndex, function (results) {
                $searchPane.removeClass("loading");

                if (OnCompleteFunc != null)
                    OnCompleteFunc(results);
            });
        });
    }

    function PrepareSearchResults(resultSet) {
        var resultArray = [];

        for (var i = 0, length = resultSet.GetLength(); i < length; i++) {
            var result = resultSet.GetResult(i);
            var searchDBID = result.SearchDB;
            var title = null;
            var linkUrl = null;
            var abstractText = null;

            if (!_HelpSystem.IsWebHelpPlus) {
                var entry = result.Entry;
                var topicID = entry.TopicID;
                var searchDB = MadCap.WebHelp.SearchPane.SearchDBs[searchDBID];
                title = searchDB.URLTitles[topicID] ? searchDB.URLTitles[topicID] : "";
                abstractText = searchDB.URLAbstracts[topicID];
                var path = searchDB.HelpSystem.GetPath();
                var file = searchDB.URLSources[topicID];
                var isFromPreMergedChildProject = MadCap.String.StartsWith(file, "/subsystems/", false);
                var isFromChildProject = !MadCap.String.IsNullOrEmpty(path) || isFromPreMergedChildProject;

                if (isFromChildProject && !_HelpSystem.MoveContentToRoot) // add "../" to search results from child projects
                    path = "../" + path;

                if (!isFromPreMergedChildProject)
                    path += "Data/";

                linkUrl = new MadCap.Utilities.Url(path).CombinePath(file);

                if (!isFromChildProject && !_HelpSystem.MoveContentToRoot)
                    linkUrl = linkUrl.ToRelative(_HelpSystem.ContentFolder);
            }
            else {
                title = result.Title;
                abstractText = result.AbstractText;
                var resultUrl = new MadCap.Utilities.Url(result.Link);
                var baseUrl = new MadCap.Utilities.Url(document.location.pathname);

                if (!MadCap.String.EndsWith(document.location.pathname, "/")) // http://MyServer/MyHTML5/ vs. http://MyServer/MyHTML5/Default.htm
                    baseUrl = baseUrl.ToFolder();

                baseUrl = baseUrl.CombinePath(_HelpSystem.ContentFolder);
                linkUrl = resultUrl.ToRelative(baseUrl);
            }

            resultArray[resultArray.length] = { Title: title, Link: linkUrl.FullPath, AbstractText: abstractText };
        }

        return resultArray;
    }

    function BuildSearchResults(searchQuery, results, communityResults) {
        var headingEl = $("#results-heading")[0];
        var length = (results != null ? results.length : 0);
        var totalLength = length + (communityResults != null ? communityResults.TotalRecords : 0);

        $(".query", headingEl).text("\"" + searchQuery + "\"");
        $(".total-results", headingEl).text(totalLength);

        var ul = document.createElement("ul");
        ul.setAttribute("id", "resultList");

        if (results == null)
            ul.setAttribute("class", "communitySearch");

        if (communityResults != null && communityResults.Activities.length > 0) {
            var li = document.createElement("li");
            li.setAttribute("id", "community-results");
            ul.appendChild(li);

            var h3 = document.createElement("h3");
            h3.setAttribute("class", "title");

            var communitySearchLink = document.createElement("a");
            communitySearchLink.setAttribute("href", "#communitysearch-" + searchQuery);
            communitySearchLink.appendChild(document.createTextNode("Community Results"));

            h3.appendChild(communitySearchLink);

            var communitySearchInfo = document.createElement("span");
            communitySearchInfo.appendChild(document.createTextNode(" (" + communityResults.TotalRecords + ")"));
            h3.appendChild(communitySearchInfo);

            var communityUl = document.createElement("ul");
            communityUl.setAttribute("id", "communityResultList");

            li.appendChild(h3);
            li.appendChild(communityUl);

            var now = new Date();
            var utcNow = new Date(now.getUTCFullYear(), now.getUTCMonth(), now.getUTCDate(), now.getUTCHours(), now.getUTCMinutes(), now.getUTCSeconds());

            for (var i = 0; i < communityResults.Activities.length; i++) {
                var communityResult = communityResults.Activities[i];

                var communityLi = document.createElement("li");
                communityUl.appendChild(communityLi);

                var communityLink = document.createElement("a");
                communityLink.setAttribute("class", "activityText");
                communityLink.setAttribute("href", "#pulse-#!streams/" + communityResult.FeedId + "/activities/" + communityResult.Id);
                communityLink.appendChild(document.createTextNode(communityResult.Text));

                var communityLinkInfo = document.createElement("div");
                communityLinkInfo.setAttribute("class", "activityInfo");

                var createdByA = document.createElement("a");
                createdByA.setAttribute("class", "activityCreator");
                createdByA.setAttribute("href", "#pulse-#!streams/" + communityResult.CreatedBy + "/activities");
                createdByA.appendChild(document.createTextNode(communityResult.CreatedByDisplayName));

                var toSpan = document.createElement("span");
                toSpan.appendChild(document.createTextNode(" to "));

                var feedUrl = communityResult.FeedUrl != null ? "#" + communityResult.FeedUrl : "#pulse-#!streams/" + communityResult.FeedId + "/activities";

                var pageA = document.createElement("a");
                pageA.setAttribute("class", "activityFeed");
                pageA.setAttribute("href", feedUrl);
                pageA.appendChild(document.createTextNode(communityResult.FeedName));

                var postedOn = new MadCap.Utilities.DateTime(communityResult.PostedUtc);
                var postedTimeSpan = new MadCap.Utilities.TimeSpan(postedOn.Date, utcNow);

                var postedOnSpan = document.createElement("span");
                postedOnSpan.setAttribute("class", "activityTime");
                postedOnSpan.appendChild(document.createTextNode(postedTimeSpan.ToDurationString()));

                communityLinkInfo.appendChild(createdByA);
                communityLinkInfo.appendChild(toSpan);
                communityLinkInfo.appendChild(pageA);
                communityLinkInfo.appendChild(postedOnSpan);

                communityLi.appendChild(communityLink);
                communityLi.appendChild(communityLinkInfo);
            }
        }

        if (results != null) {
            for (var i = 0; i < results.length; i++) {
                var result = results[i];
                var title = result.Title;
                var link = result.Link;
                var abstractText = result.AbstractText;

                var li = document.createElement("li");
                ul.appendChild(li);

                var h3 = document.createElement("h3");
                $(h3).addClass("title");
                li.appendChild(h3);

                var a = document.createElement("a");
                a.setAttribute("href", "#" + link + "?Highlight=" + searchQuery);
                a.appendChild(document.createTextNode(title));
                h3.appendChild(a);

                if (abstractText != null) {
                    var divDesc = document.createElement("div");
                    $(divDesc).addClass("description");
                    divDesc.appendChild(document.createTextNode(abstractText));
                    li.appendChild(divDesc);
                }

                var divUrl = document.createElement("div");
                $(divUrl).addClass("url");
                li.appendChild(divUrl);

                var cite = document.createElement("cite");
                cite.appendChild(document.createTextNode(link));
                divUrl.appendChild(cite);
            }
        }

        $(ul).appendTo($("#searchPane"));

        if (_HelpSystem.LiveHelpEnabled) {
            _FeedbackController.LogSearch(_HelpSystem.LiveHelpOutputId, null, length, null, searchQuery);
        }
    }

    function NavigationResizeBar_MouseDown(e) {
        MadCap.DEBUG.Log.AddLine("nav resizeBar : mousedown");

        if ($(e.target).attr("id") == "show-hide-navigation")
            return;

        if ($(this).hasClass("nav-closed"))
            return;

        var sheetEl = document.createElement("div");
        sheetEl.setAttribute("id", "mousemove-sheet");
        document.body.appendChild(sheetEl);

        $(document).mousemove(NavigationResizeBar_MouseMove);
        $(document).mouseup(NavigationResizeBar_MouseUp);
        $(document).bind("selectstart", NavigationResizeBar_SelectStart); // For IE 8 and below only. Prevent text selection.

        e.preventDefault(); // prevent text selection
    }

    function NavigationResizeBar_SelectStart(e) {
        return false;
    }

    function NavigationResizeBar_MouseMove(e) {
        MadCap.DEBUG.Log.AddLine("nav resizeBar : mousemove : " + e.pageX);

        var panePos = $(document.documentElement).hasClass("left-layout") ? "left" : $(document.documentElement).hasClass("right-layout") ? "right" : "left";
        var width = e.pageX;

        if (panePos == "right")
            width = window.innerWidth - e.pageX;

        ResizeNavigation(width);
    }

    function NavigationResizeBar_MouseUp(e) {
        MadCap.DEBUG.Log.AddLine("nav resizeBar : mouseup");

        $(document).off("mousemove", NavigationResizeBar_MouseMove);
        $(document).off("mouseup", NavigationResizeBar_MouseUp);
        $(document).off("selectstart", NavigationResizeBar_SelectStart);

        // IE needs this in a setTimeout(). Otherwise, you need to click the mouse again before you can select text, resize the resize bar, etc.
        var sheetEl = $("#mousemove-sheet")[0];
        window.setTimeout(function () { sheetEl.parentNode.removeChild(sheetEl); }, 1);
    }

    function ResizeNavigation(width) {
        var panePos = $(document.documentElement).hasClass("left-layout") ? "left" : $(document.documentElement).hasClass("right-layout") ? "right" : "left";

        if (panePos == "left") {
            if (width < 175 || width > (window.innerWidth * 0.85))
                return;
        }
        else if (panePos == "right") {
            if (width < (window.innerWidth * 0.15) || width > (window.innerWidth - 175))
                return;
        }

        AdjustTabs(width);

        $("#navigationResizeBar").css(panePos, width + "px");
        $("#navigation").css("width", width + "px");
        $("#contentBody").css(panePos, (width + 5) + "px");
    }

    function AdjustTabs(width) {
        var tabs = $(".tabs-nav li");
        $.each(tabs, function (index, item) {
            var li = $(item);
            if (li.hasClass("tab-collapsed"))
                li.removeClass("tab-collapsed");
        });
        if (width < CalculateTabsWidth() + 4) {
            for (var index = tabs.length - 1; index >= 0; index--) {
                var li = $(tabs[index]);
                li.addClass("tab-collapsed");
                if (width > CalculateTabsWidth() + 18) {
                    break;
                }
            }
        }
    }

    function CalculateTabsWidth() {
        var width = 0;
        var tabs = $(".tabs-nav li");
        tabs.each(function (index, li) {
            var tab = $(li);
            width += parseInt(tab.css("width"));
        });

        return width;
    }

    function ShowHideNavigation_Click(e) {
        var $navigation = $("#navigation");

        if (!$navigation.hasClass("nav-closed"))
            ShowHideNavigation("hide");
        else
            ShowHideNavigation("show");
    }

    function ShowHideNavigation(which) {
        var panePos = $(document.documentElement).hasClass("left-layout") ? "left" : $(document.documentElement).hasClass("right-layout") ? "right" : "left";

        var $navigation = $("#navigation");
        var $navigationResizeBar = $("#navigationResizeBar");
        var $contentBody = $("#contentBody");

        if (which == "show") {
            $contentBody.css(panePos, $contentBody.attr("data-mc-last-width"));
            $navigationResizeBar.css(panePos, $navigationResizeBar.attr("data-mc-last-width"));

            $navigation.removeClass("nav-closed");
            $navigationResizeBar.removeClass("nav-closed");
            $contentBody.removeClass("nav-closed");
        }
        else if (which == "hide") {
            $contentBody.attr("data-mc-last-width", $contentBody.css(panePos)); // store current position
            $contentBody.css(panePos, "5px");

            $navigationResizeBar.attr("data-mc-last-width", $navigationResizeBar.css(panePos)); // store current position
            $navigationResizeBar.css(panePos, 0);

            $navigation.addClass("nav-closed");
            $navigationResizeBar.addClass("nav-closed");
            $contentBody.addClass("nav-closed");
        }
    }

    function LoadFromHash() {
        if (document.location.hash.length == 0)
            return;

        if (MadCap.String.Contains(document.location.hash, "javascript:") || MadCap.String.Contains(document.location.hash, "data:") || MadCap.String.Contains(document.location.hash, "<script>")) {
            document.location.hash = "";
            return;
        }

        var topicPath = document.location.hash.substring(1);
        topicPath = unescape(topicPath);

        if (MadCap.String.Contains(topicPath, "cshid=") || MadCap.String.Contains(topicPath, "searchQuery=") || MadCap.String.Contains(topicPath, "skinName=")) {
            LoadCshFromHash();

            return;
        }
        else if (MadCap.String.StartsWith(topicPath, "search-")) {
            var searchQuery = topicPath.substring("search-".length);

            $("#search-field").val(searchQuery); // set the value of the search field. This needs to happen when the search originated directly from the URL rather than by typing in the search field and submitting.

            DoSearch(searchQuery);

            return;
        }
        else if (MadCap.String.StartsWith(topicPath, "communitysearch-")) {
            var searchQuery = topicPath.substring("communitysearch-".length);

            $("#search-field").val(searchQuery);

            DoSearch(searchQuery, false, true, -1, 0);

            return;
        }
        else if (MadCap.String.StartsWith(topicPath, "pulse-")) {
            var pulsePath = topicPath.substring("pulse-".length);

            LoadStream(pulsePath);

            return;
        }

        LoadTopic(topicPath);
    }

    function LoadTopic(path) {
        /// <summary>Loads a topic into the topic pane.</summary>
        /// <param name="path">The path of the topic relative to the Content folder.</param>

        var pathUrl = new MadCap.Utilities.Url(path).ToNoQuery();

        if (pathUrl.IsAbsolute)
            path = pathUrl.FullPath;
        else
            path = _HelpSystem.ContentFolder + pathUrl.FullPath;

        LoadFile(path);
    }

    function LoadFile(path) {
        /// <summary>Loads a file into the topic pane.</summary>
        /// <param name="path">The path of the file.</param>

        $(document.documentElement).addClass('has-topic');

        ShowPane("topic");

        // IE9 Bug for loading pdfs into a frame workaround
        // http://www.digiblog.de/2011/08/ie9-bug-loading-pdfs-into-frames-using-javascript/
        if ($.browser.msie)
            document.getElementById("topic").src = path;
        else
            frames["topic"].location.replace(path);

        var href = new MadCap.Utilities.Url(unescape(document.location.href));
        var tocType = null, tocPath = null, bsPath = null;

        if (!MadCap.String.IsNullOrEmpty(href.Fragment) && href.Fragment.length > 1) {
            tocPath = href.QueryMap.GetItem('TocPath');

            if (tocPath != null) {
                tocType = 'Toc';
            }
            else {
                bsPath = href.QueryMap.GetItem('BrowseSequencesPath');

                if (bsPath != null) {
                    tocType = 'BrowseSequences';
                }
            }

            if (href.HashMap.GetItem('cshid') == null) {
                href = new MadCap.Utilities.Url(href.Fragment.substr(1));
            }
        }
        else {
            href = new MadCap.Utilities.Url(_HelpSystem.DefaultStartTopic).ToRelative(_HelpSystem.GetContentPath());
        }

        _HelpSystem.SetBrowseSequencePath(bsPath, href);

        if (_HelpSystem.SyncTOC) {
            MadCap.Utilities.CrossFrame.PostMessageRequest(parent, 'sync-toc', [tocType, tocType == 'Toc' ? tocPath : bsPath, href.FullPath], null);
        }
    }

    function LoadStream(url) {
        /// <summary>Loads a stream into the Pulse pane.</summary>
        /// <param name="url">The stream url.</param>

        $(document.documentElement).removeClass('has-topic');

        ShowPane("pulse");

        var hash = url.substring(url.indexOf('#'));

        MadCap.Utilities.CrossFrame.PostMessageRequest(frames["community-frame-html5"], "pulse-hash-changed", [hash]);

        _FeedbackController.Init(function () {
            if (_FeedbackController.PulseActive)
                frames["pulse"].location.replace(_FeedbackController.PulseServer + hash);
        });
    }

    function LoadCshFromHash() {
        var hash = document.location.hash.substring(1);
        var hashMap = new MadCap.Utilities.Dictionary();
        var pairs = hash.split("&");
        $(pairs).each(function (index, value) {
            var kvp = pairs[index].split("=");
            hashMap.Add(kvp[0].toLowerCase(), kvp[1]); // case insensitive
        });

        var searchQuery = hashMap.GetItem("searchQuery".toLowerCase());

        if (searchQuery != null) {
            $("#search-field").val(searchQuery); // set the value of the search field

            var firstPick = MadCap.String.ToBool(hashMap.GetItem("firstPick".toLowerCase()), false);

            if (firstPick) {
                Search(searchQuery, null, function (results) {
                    if (results.length >= 1)
                        LoadTopic(results[0].Link);
                });
            }
            else {
                DoSearch(searchQuery);
            }
        }
        else {
            var cshid = hashMap.GetItem("cshid");

            if (cshid != null) {
                _CSHID = cshid;

                _HelpSystem.LookupCSHID(cshid, function (idInfo) {
                    if (idInfo.Found)
                        LoadFile(idInfo.Topic);
                    else
                        LoadFile(_HelpSystem.DefaultStartTopic);

                    var skinName = hashMap.GetItem("skinName".toLowerCase()) || idInfo.Skin;

                    if (skinName != null) {
                        var skin = _HelpSystem.GetSkin(skinName);

                        ApplySkin(skin);
                    }
                });

                return;
            }
            else {
                LoadFile(_HelpSystem.DefaultStartTopic);
            }
        }

        var skinName = hashMap.GetItem("skinName".toLowerCase());

        if (skinName != null) {
            var skin = _HelpSystem.GetSkin(skinName);

            ApplySkin(skin);
        }
    }

    function GetPulsePathFromHash() {
        if (document.location.hash.indexOf("#pulse-") != 0)
            return "";

        return document.location.hash.substring("#pulse-".length);
    }

    function ApplySkin(skin) {
        SetSize(skin);

        if (MadCap.String.IsNullOrEmpty(skin.Tabs)) {
            $("#navigation").remove();
            $("#navigationResizeBar").remove();
            $(document.documentElement).removeClass("left-layout").removeClass("right-layout");
        }
        else {
            if (skin.WebHelpOptions != null && skin.WebHelpOptions.HideNavigationOnStartup != null && (MadCap.String.ToBool(skin.WebHelpOptions.HideNavigationOnStartup, false)))
                ShowHideNavigation("hide");

            if (skin.NavigationPanePosition != null && skin.NavigationPanePosition == "Right")
                $(document.documentElement).removeClass("left-layout").addClass("right-layout");

            if (skin.NavigationPaneWidth != null) {
                var navWidth = MadCap.String.ToInt(skin.NavigationPaneWidth, 300);

                ResizeNavigation(navWidth);
            }

            var tabs = skin.Tabs.split(",");
            var allTabs = ["TOC", "Index", "Glossary", "BrowseSequences", "Community"];
            var $tabsEl = $(".tabs");

            for (var i = 0, length = allTabs.length; i < length; i++) {
                var tab = allTabs[i];

                if ($.inArray(tab, tabs) >= 0)
                    continue;

                if (tab == "TOC") tab = "Toc";

                var $tab = $("#" + tab + "Tab");

                if ($tab.length == 0)
                    continue;

                var tabIndex = $tabsEl.children(".tabs-nav").children("li").index($tab); // can't use $tab.index() because CSS3PIE adds elements between the <li> elements in IE 8.
                var $panelEl = $tabsEl.children(".tabs-panels").children(":eq(" + tabIndex + ")");
                $tab.remove();
                $panelEl.remove();
            }

            var defaultTab = skin.DefaultTab;
            if (defaultTab == "TOC") defaultTab = "Toc";
            SetActivePane(defaultTab, $tabsEl);
            LoadPane(defaultTab);
        }

        if (skin.Toolbar != null && MadCap.String.IsNullOrEmpty(skin.Toolbar.Buttons)) {
            $(".buttons").remove();
            $("#contentBody").addClass("no-buttons");
        }

        if (skin.DisplaySearchBar == "false")
            $(".search-bar").hide();
    }

    function ShowPane(pane) {
        $("#topic").css("display", pane == "topic" ? "block" : "none");
        $("#pulse").css("display", pane == "pulse" ? "block" : "none");
        $("#searchPane").css("display", pane == "search" ? "block" : "none");
    }

    function NavTabs_Click(e) {
        var tabID = $(this).attr("id");
        var name = tabID.substring(0, tabID.length - "Tab".length);

        SetActivePane(name, $(this).closest('.tabs'));

        // Load the pane
        LoadPane(name);
    }

    function SetActivePane(name, $tabsEl) {
        // set currently active tab to inactive
        var $activeTabEl = $(".tabs-nav-active", $tabsEl);
        $activeTabEl.removeClass("tabs-nav-active");

        // set new tab to active
        var $newActiveTab = $("#" + name + "Tab");
        $newActiveTab.addClass("tabs-nav-active");

        // set currently active panel to inactive
        var $activePanelEl = $(".tabs-panel-active", $tabsEl);
        $activePanelEl.removeClass("tabs-panel-active");

        // set new panel to active
        var tabIndex = $tabsEl.children(".tabs-nav").children("li").index($newActiveTab); // can't use $tabsEl.index() because CSS3PIE adds elements between the <li> elements in IE 8.
        var $panelEl = $tabsEl.children(".tabs-panels").children(":eq(" + tabIndex + ")");
        $panelEl.addClass("tabs-panel-active");
    }

    function LoadDefaultPane() {
        var name = _HelpSystem.DefaultSkin.DefaultTab;

        if (name == "TOC")
            LoadPane("Toc");
        else
            LoadPane(name);
    }

    function LoadPane(name) {
        if (name == "Toc")
            LoadToc();
        else if (name == "Index")
            LoadIndex();
        else if (name == "Glossary")
            LoadGlossary();
        else if (name == "BrowseSequences")
            LoadBrowseSequences();
        else if (name == "Community")
            LoadCommunity();
    }

    function LoadToc() {
        if (_TocPane != null)
            return;

        var $pane = $("#toc");
        $pane.addClass("loading");

        _TocPane = new MadCap.WebHelp.TocPane("Toc", _HelpSystem, $pane[0]);
        _TocPane.Init(function () {
            $pane.removeClass("loading");
        });
    }

    function LoadIndex() {
        if (_IndexPane != null)
            return;

        var $pane = $("#index");
        $pane.addClass("loading");

        _IndexPane = new MadCap.WebHelp.IndexPane(_HelpSystem);
        _IndexPane.Init($("#index .index-wrapper")[0], function () {
            $pane.removeClass("loading");
        });
    }

    function LoadGlossary() {
        if (_GlossaryPane != null)
            return;

        var $pane = $("#glossary");
        $pane.addClass("loading");

        _GlossaryPane = new MadCap.WebHelp.GlossaryPane(_HelpSystem);
        _GlossaryPane.Init($pane[0], function () {
            $pane.removeClass("loading");
        });
    }

    function LoadBrowseSequences() {
        if (_BrowseSequencesPane != null)
            return;

        var $pane = $("#browseSequences");
        $pane.addClass("loading");

        _BrowseSequencesPane = new MadCap.WebHelp.TocPane("BrowseSequences", _HelpSystem, $pane[0]);
        _BrowseSequencesPane.Init(function () {
            $pane.removeClass("loading");
        });
    }

    function LoadCommunity() {
        if (_CommunityLoaded)
            return;

        _CommunityLoaded = true;

        var $comFrame = $("#community-frame-html5");

        _FeedbackController.Init(function () {
            if (_FeedbackController.PulseActive)
                $comFrame.attr("src", _FeedbackController.PulseServer + "streams/my");
        });
    }

    function SetSize(skin) {
        var useDefaultSize = MadCap.String.ToBool(skin.UseBrowserDefaultSize, false);

        if (useDefaultSize)
            return;

        var topPx = MadCap.String.ToInt(skin.Top, 0);
        var leftPx = MadCap.String.ToInt(skin.Left, 0);
        var bottomPx = MadCap.String.ToInt(skin.Bottom, 0);
        var rightPx = MadCap.String.ToInt(skin.Right, 0);
        var widthPx = MadCap.String.ToInt(skin.Width, 800);
        var heightPx = MadCap.String.ToInt(skin.Height, 600);

        var anchors = skin.Anchors;

        if (anchors) {
            var aTop = (anchors.indexOf("Top") > -1) ? true : false;
            var aLeft = (anchors.indexOf("Left") > -1) ? true : false;
            var aBottom = (anchors.indexOf("Bottom") > -1) ? true : false;
            var aRight = (anchors.indexOf("Right") > -1) ? true : false;
            var aWidth = (anchors.indexOf("Width") > -1) ? true : false;
            var aHeight = (anchors.indexOf("Height") > -1) ? true : false;
        }

        if (aLeft && aRight)
            widthPx = screen.availWidth - (leftPx + rightPx);
        else if (!aLeft && aRight)
            leftPx = screen.availWidth - (widthPx + rightPx);
        else if (aWidth)
            leftPx = (screen.availWidth / 2) - (widthPx / 2);

        if (aTop && aBottom)
            heightPx = screen.availHeight - (topPx + bottomPx);
        else if (!aTop && aBottom)
            topPx = screen.availHeight - (heightPx + bottomPx);
        else if (aHeight)
            topPx = (screen.availHeight / 2) - (heightPx / 2);

        if (window == top) {
            window.resizeTo(widthPx, heightPx);
            window.moveTo(leftPx, topPx);
        }
    }

    function UpdateRating() {
        $(".star-buttons").addClass("loading");

        _FeedbackController.GetAverageRating(_TopicID, function (averageRating, ratingCount) {
            $(".star-buttons").removeClass("loading");

            SetFeedbackRating(averageRating);
        });
    }

    function SetFeedbackRating(rating) {
        var $starContainer = $(".star-buttons");
        var $stars = $(".star-button", $starContainer);
        var starCount = $stars.length;
        var numIcons = Math.ceil(rating * starCount / 100);

        $stars.css("opacity", 0);

        for (var i = 0; i < starCount; i++) {
            var starButton = $stars[i];
            var $starButton = $(starButton);

            window.setTimeout((function (i, $starButton) {
                return function () {
                    if (i <= numIcons - 1)
                        SetButtonState($starButton[0], 2);
                    else
                        SetButtonState($starButton[0], 1);

                    $starButton.animate({ opacity: 1 });
                }
            })(i, $starButton), i * 50);
        }
    }

    function FeedbackRating_Click(e) {
        var $target = $(e.target);

        if ($target.hasClass("star-button")) {
            var starCount = $(".star-button", this).length;
            var rating = ($target.index() + 1) * 100 / starCount;

            _FeedbackController.SubmitRating(_TopicID, rating, null, function () {
                UpdateRating();
            });
        }
    }

    function AdvanceTopic(moveType) {
        GetAdvanceUrl(moveType, function (href) {
            if (href) {
                document.location.hash = href;
            }
        });
    }

    function PreviousTopic() {
        AdvanceTopic("previous");
    }

    function NextTopic() {
        AdvanceTopic("next");
    }

    function GetAdvanceUrl(moveType, CallBackFunc) {
        MadCap.Utilities.CrossFrame.PostMessageRequest(frames["topic"], "get-topic-url", null, function (data) {
            var href = new MadCap.Utilities.Url(unescape(data[0]));
            var root = new MadCap.Utilities.Url(unescape(document.location.href));

            var tocPath = root.QueryMap.GetItem('TocPath');
            var bsPath = root.QueryMap.GetItem('BrowseSequencesPath');

            root = root.ToPlainPath();
            if (!root.IsFolder)
                root = root.ToFolder();

            var contentFolder = root.CombinePath(_HelpSystem.GetMasterHelpsystem().GetContentPath());
            href = href.ToRelative(contentFolder);

            if (bsPath != null) {
                _HelpSystem.AdvanceTopic("BrowseSequences", moveType, bsPath, href, CallBackFunc);
            }
            else {
                _HelpSystem.AdvanceTopic("Toc", moveType, tocPath, href, CallBackFunc);
            }
        });
    }

    function UpdateCurrentTopicIndex() {
        //        var span = document.getElementById("MCCurrentTopicIndexContainer");

        //        if (span == null)
        //        {
        //            return;
        //        }

        //        if (MCGlobals.InPreviewMode)
        //        {
        //            SetCurrentTopicIndexSequenceIndex(0);
        //            SetCurrentTopicIndexTotal(0);
        //            OnCompleteBoth();
        //        }
        //        else
        {
            MadCap.Utilities.CrossFrame.PostMessageRequest(frames["topic"], "get-bs-path", null, function (data) {
                function OnCompleteGetEntrySequenceIndex(sequenceIndex) {
                    var $currentTopicIndex = $(".current-topic-index-button");

                    if (sequenceIndex == -1) {
                        $currentTopicIndex.addClass("disabled");

                        return;
                    }

                    $currentTopicIndex.removeClass("disabled");

                    $(".sequence-index").text(sequenceIndex);

                    file.GetIndexTotalForEntry(bsPath, href, function (total) {
                        $(".sequence-total").text(total);
                    });
                }

                var bsPath = data[0];
                var href = new MadCap.Utilities.Url(unescape(data[1]));
                var homeUrl = new MadCap.Utilities.Url(unescape(document.location.href));
                homeUrl = new MadCap.Utilities.Url(homeUrl.PlainPath);
                var homeFolder = MadCap.String.EndsWith(homeUrl.FullPath, "/") ? homeUrl : homeUrl.ToFolder(); // Don't need .ToFolder() in the case that the page URL ends in a '/' (could happen when located on a web server: http://mydomain.com/WebHelp2/)
                href = href.ToRelative(homeFolder);

                if (bsPath != null) {
                    var fullBsPath = _HelpSystem.GetFullTocPath("browsesequences", href.FullPath);

                    if (fullBsPath)
                        bsPath = bsPath ? fullBsPath + "|" + bsPath : fullBsPath;
                }

                if (MadCap.String.IsNullOrEmpty(bsPath) || MadCap.String.StartsWith(bsPath, "_____")) {
                    OnCompleteGetEntrySequenceIndex(-1);

                    return;
                }

                var file = _HelpSystem.GetBrowseSequenceFile();
                file.GetEntrySequenceIndex(bsPath, href, OnCompleteGetEntrySequenceIndex);
            });
        }
    }

    function ToggleButtonState(buttonEl) {
        var $buttonEl = $(buttonEl);
        var currState = $buttonEl.attr("data-current-state") || "1";
        var nextState = currState == "1" ? 2 : 1;

        SetButtonState(buttonEl, nextState)
    }

    function SetButtonState(buttonEl, newState) {
        var $buttonEl = $(buttonEl);
        var currState = newState == 1 ? 2 : 1;
        var newStateClass = $buttonEl.attr("data-state" + newState + "-class");
        var currStateClass = $buttonEl.attr("data-state" + currState + "-class");

        $buttonEl.attr("data-current-state", newState);
        $buttonEl.removeClass(currStateClass).addClass(newStateClass);
        $buttonEl.attr("title", $buttonEl.attr("data-state" + newState + "-title"));
    }

    function UpdateLoginButton() {
        _UserGuid = _FeedbackController.GetUserGuid();

        var $el = $('.login-button');
        if ($el.length == 0)
            $el = $('.edit-user-profile-button');

        SetButtonState($el[0], _UserGuid == null ? 1 : 2);
    }

    function CloseLoginDialog() {
        if (_LoginDialog != null) {
            _LoginDialog.Hide(true);
        }
    }

    MadCap.Utilities.CrossFrame.AddMessageHandler(function (message, dataValues, responseData, messageSource, messageID) {
        var returnData = { Handled: false, FireResponse: true };

        if (message == "get-href") {
            responseData[responseData.length] = document.location.href;

            //

            returnData.Handled = true;
            returnData.FireResponse = true;
        }
        if (message == "get-return-url") {
            var url = new MadCap.Utilities.Url(document.location.href);
            var returnUrl = null;

            if (url.Fragment.length > 1) {
                var href = new MadCap.Utilities.Url(url.Fragment.substring(1));
                returnUrl = url.QueryMap.GetItem('returnUrl');
            }

            responseData[responseData.length] = returnUrl;

            returnData.Handled = true;
            returnData.FireResponse = true;
        }
        else if (message == "navigate") {
            var path = dataValues[0];

            if (path) {
                document.location.hash = path;
            }

            returnData.Handled = true;
            returnData.FireResponse = true;
        }
        else if (message == "navigate-topic") {
            var path = dataValues[0];

            var href = new MadCap.Utilities.Url(path);

            if (href.IsAbsolute) {
                // path will be absolute so make it relative to the home folder
                var homeUrl = new MadCap.Utilities.Url(document.location.href);
                homeUrl = new MadCap.Utilities.Url(homeUrl.PlainPath);
                var homeFolder = MadCap.String.EndsWith(homeUrl.FullPath, "/") ? homeUrl : homeUrl.ToFolder(); // Don't need .ToFolder() in the case that the page URL ends in a '/' (could happen when located on a web server: http://mydomain.com/WebHelp2/)
                var contentFolder = homeFolder.CombinePath(_HelpSystem.ContentFolder);
                href = href.ToRelative(contentFolder);
            }

            document.location.hash = href.FullPath;

            returnData.Handled = true;
        }
        else if (message == "navigate-home") {
            var url = new MadCap.Utilities.Url(document.location.href);

            document.location.href = url.PlainPath;

            returnData.Handled = true;
        }
        else if (message == "navigate-pulse") {
            var path = dataValues[0];

            // append returnUrl if register/forgotpassword
            if (document.location.hash.length > 1 && path) {
                var lowerPath = path.toLowerCase();

                if (lowerPath === 'feedback/account/register' || path.toLowerCase() === 'forgotpassword') {
                    var url = new MadCap.Utilities.Url(document.location.hash.substring(1));
                    var returnUrl = url.QueryMap.GetItem('returnUrl');

                    if (returnUrl != null) {
                        returnUrl = escape(returnUrl);
                    }
                    else {
                        returnUrl = document.location.hash.substring(1);
                    }

                    path += '?returnUrl=' + returnUrl;
                }
            }

            document.location.hash = "pulse-" + path;

            returnData.Handled = true;
        }
        else if (message == "navigate-previous") {
            PreviousTopic();

            returnData.Handled = true;
        }
        else if (message == "navigate-next") {
            NextTopic();

            returnData.Handled = true;
        }
        else if (message == "login-user" || message == "login-pulse") {
            if (_UserGuid == null) {
                var mode = message == "login-pulse" ? "pulse" : "new";
                _LoginDialog = new MadCap.Feedback.LoginDialog(_FeedbackController, mode);

                if (mode == "new") {
                    $(_LoginDialog).bind("closed", function () {
                        UpdateLoginButton();

                        responseData[responseData.length] = _UserGuid;

                        MadCap.Utilities.CrossFrame._PostMessageResponse(messageSource, message, responseData.length > 0 ? responseData : null, messageID);
                    });
                }

                _LoginDialog.Show();

                //

                returnData.Handled = true;
                returnData.FireResponse = false;
            }
            else {
                responseData[responseData.length] = _UserGuid;

                //

                returnData.Handled = true;
                returnData.FireResponse = true;
            }
        }
        else if (message == "get-csh-id") {
            responseData[responseData.length] = _CSHID;

            //

            returnData.Handled = true;
            returnData.FireResponse = true;
        }
        else if (message == "get-user-guid") {
            responseData[responseData.length] = _UserGuid;

            //

            returnData.Handled = true;
            returnData.FireResponse = true;
        }
        else if (message == "get-topic-path-by-stream-id") {
            var streamID = dataValues[0];

            _FeedbackController.GetTopicPathByStreamID(streamID, function (topicPath) {
                responseData[responseData.length] = topicPath;

                MadCap.Utilities.CrossFrame._PostMessageResponse(messageSource, message, responseData.length > 0 ? responseData : null, messageID);
            }, null, null);

            //

            returnData.Handled = true;
            returnData.FireResponse = false;
        }
        else if (message == "get-topic-path-by-page-id") {
            var pageID = dataValues[0];

            _FeedbackController.GetTopicPathByPageID(pageID, function (topicPath) {
                responseData[responseData.length] = topicPath;

                MadCap.Utilities.CrossFrame._PostMessageResponse(messageSource, message, responseData.length > 0 ? responseData : null, messageID);
            }, null, null);

            //

            returnData.Handled = true;
            returnData.FireResponse = false;
        }
        else if (message == "hash-changed") {
            var newHash = dataValues[0];
            newHash = newHash.substring(1);

            history.pushState(null, null, document.location.pathname + document.location.hash + "$" + newHash);

            //

            returnData.Handled = true;
            returnData.FireResponse = false;
        }
        else if (message == "forward-ajax-open-success") {
            var data = dataValues[0];
            var status = parseInt(dataValues[1]);
            var dest = dataValues[2];

            ShowPane("pulse");

            MadCap.Utilities.CrossFrame.PostMessageRequest(frames["pulse"], "ajax-open-success", [data, status, dest]);

            //

            returnData.Handled = true;
            returnData.FireResponse = false;
        }
        else if (message == "get-pulse-hash") {
            var pulseHash = "";

            if (document.location.hash.indexOf('#pulse-') == 0)
                pulseHash = document.location.hash.substring('#pulse-'.length);

            responseData[responseData.length] = pulseHash;

            returnData.Handled = true;
            returnData.FireResponse = true;
        }
        else if (message == "login-complete" || message == "logout-complete") {
            MadCap.Utilities.CrossFrame.PostMessageRequest(frames["pulse"], "reload");
            MadCap.Utilities.CrossFrame.PostMessageRequest(frames["community-frame-html5"], "reload");

            MadCap.Utilities.CrossFrame.PostMessageRequest(frames["topic"], "reload-pulse");

            CloseLoginDialog();
            UpdateLoginButton();

            returnData.Handled = true;
            returnData.FireResponse = false;
        }
        else if (message == "close-login-dialog") {
            CloseLoginDialog();

            returnData.Handled = true;
            returnData.FireResponse = false;
        }
        else if (message == "set-pulse-login-id") {
            if (_FeedbackController != null)
                _FeedbackController.PulseUserGuid = dataValues[0];

            UpdateLoginButton();

            returnData.Handled = true;
            returnData.FireResponse = false;
        }

        return returnData;
    }, null);

    $(Window_Onload);
    $(window).hashchange(Window_Onhashchange); // hashchange polyfill

    var _TocPane = null;
    var _IndexPane = null;
    var _SearchPane = null;
    var _GlossaryPane = null;
    var _BrowseSequencesPane = null;
    var _CommunityLoaded = null;
    var _HelpSystem = null;
    var _FeedbackController = null;
    var _TopicID = null;
    var _UserGuid = null;
    var _CSHID = null;
    var _LoginDialog = null;
})();
