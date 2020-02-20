(function() {
    function addEvent(element, eventName, fn) {
        if (element.addEventListener)
            element.addEventListener(eventName, fn, false);
        else if (element.attachEvent)
            element.attachEvent('on' + eventName, fn);
    }

    addEvent(window, 'load', function(){
        document.querySelectorAll('.rst-widget-sidebar .rst-widget-header + .rst-widget-body').forEach(function(e) {
            e.previousElementSibling.onclick = function() { e.classList.toggle('shift-up'); };
        })
    });
})();
