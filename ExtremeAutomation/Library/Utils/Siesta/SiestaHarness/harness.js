var harness = new Siesta.Harness.Browser.ExtJS();

harness.testClass = EmcUtils;

harness.configure({
    title: 'Siesta Harness',
    preload: ['siesta/docs/extjs/ext-all.js'],
    waitForTimeout: 60000,
    viewportWidth: 1850,
    viewportHeight: 875,
    autoScrollElementsIntoView: true,
});

harness.start(
    {
        group: 'Tests',
        expanded: true,
        separateContext: true,
        items: [
            {
                url: 'harness_case.js',
                name: 'Siesta Harness',
                pageUrl: 'https://127.0.0.1:8443/OneView/home?notop=true',
                separateContext: true
            },
        ]
    }
);
