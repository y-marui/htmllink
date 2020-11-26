// ==UserScript==
// @name         Google Drive - htmllink
// @namespace    https://github.com/y-marui/htmllink
// @version      1.0.1
// @author       @y-marui
// @description  Modify .html file preview in Google Drive
// @updateURL    https://raw.githubusercontent.com/y-marui/htmllink/main/userscript/google-drive-htmllink.js
// @downloadURL  https://raw.githubusercontent.com/y-marui/htmllink/main/userscript/google-drive-htmllink.js
// @supportURL   https://github.com/y-marui/htmllink/issues
// @match        https://drive.google.com/drive/u/*
// @grant        none
// ==/UserScript==

(function () {
    'use strict';

    var updater = function () {
        var res = document.getElementsByClassName("a-b-cg-Zf");
        if (res.length > 0 && res[0].textContent.endsWith(".html")) {
            res = document.getElementsByClassName("a-b-r-La");
            if (res.length > 0 && (res[0].getAttribute("convert") == undefined)) {
                var elem = res[0];
                elem.setAttribute("convert", true);
                elem.innerHTML = elem.textContent;
            }
        }
    }
    window.addEventListener("message", updater);
})();
