var FontActiveEvent = new Event("fontActive");
WebFont.load({
    active: function() {
        document.dispatchEvent(FontActiveEvent);
    },
    google: {
        families: ['Open Sans:400,700', 'Open Sans Condensed:300']
    }
});