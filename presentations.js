
let presentations = [
    {
        title: "Unit Conversion in Swift",
        desc: "Knoxville CocoaHeads Meetup in Knoxville, TN on April 29, 2019",
        url: "presentations/19-04-knoxcocoa-unitconv.pdf"
    },
    {
        title: "Combining high and low-order computational models to simulate biomass fast pyrolysis reactors",
        desc: "AIChE Spring Meeting and 8th World Congress on Particle Technology in Orlando, FL on April 23, 2018",
        url: "presentations/18-04-aiche-wcpt-orlando.pdf"
    },
    {
        title: "Scraping with Selenium",
        desc: "KnoxPy Meetup in Knoxville, TN on April 5, 2018",
        url: "http://slides.com/wigging/selenium"
    },
    {
        title: "Realm Mobile Database",
        desc: "Knoxville CocoaHeads Meetup in Knoxville, TN on April 18, 2017",
        url: "presentations/17-04-knoxcocoa-realm.pdf"
    },
    {
        title: "Modeling the impact of biomass particle size distribution and shape on heating behavior during fast pyrolysis",
        desc: "TCS 2016 Symposium in Chapel Hill, NC on November 1, 2016",
        url: "presentations/16-11-tcs-chapelhill.pdf"
    },
    {
        title: "Modeling the impact of biomass particle residence time on fast pyrolysis yield and composition",
        desc: "AIChE Annual Meeting in San Francisco, CA on November, 13, 2016",
        url: "presentations/16-11-aiche-sanfran.pdf"
    },
    {
        title: "Firebase for iOS",
        desc: "Knoxville CocoaHeads in Knoxville, TN on August 16, 2016",
        url: "presentations/16-08-knoxcocoa-firebase.pdf"
    },
    {
        title: "NSUserDefaults in Swift",
        desc: "Knoxville CocoaHeads in Knoxville, TN on April 19, 2016",
        url: "presentations/16-04-knoxcocoa-nsuserdefaults.pdf"
    },
    {
        title: "Low-order modeling of biomass particle mixing and reaction in a bubbling-bed fast pyrolysis reactor",
        desc: "AIChE 2014 Annual Meeting in Atlanta, GA on November 20, 2014",
        url: "presentations/14-11-aiche-atlanta.pdf"
    },
    {
        title: "Particle-scale computational modeling of woody biomass pyrolysis",
        desc: "TCS 2014 Symposium in Denver, CO on September 4, 2014",
        url: "presentations/14-09-tcs-denver.pdf"
    }
];

for (let pres of presentations) {
    var pElement = document.createElement('p');
    var title = '<b>' + pres.title + '</b>';
    var desc = pres.desc;
    if (pres.url.includes('pdf')) {
        var url = `<a href=${pres.url}>Download PDF</a>`;
    } else {
        var url = `<a href=${pres.url}>View Online</a>`;
    }
    pElement.innerHTML = `${title}. ${desc}. ${url}`;
    document.getElementById('pres').appendChild(pElement);
}
