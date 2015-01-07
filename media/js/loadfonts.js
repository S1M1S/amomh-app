var FontActiveEvent = new Event("fontActive");
WebFont.load({
    active: function () {
        document.dispatchEvent(FontActiveEvent);
    },
    google: {
        families: [
            'Raleway:100,300',
            'Open Sans:400,700',
        ]
    }
});