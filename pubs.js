
let pubs = [
    {
        title: "Integrated Particle- and Reactor-Scale Simulation of Pine Pyrolysis in a Fluidized Bed",
        desc: "Energy & Fuels, 32 (10), pp. 10683-10694, 2018",
        url: "https://pubs.acs.org/doi/abs/10.1021/acs.energyfuels.8b02309"
    },
    {
        title: "Chemics-Reactors: A Preliminary Python Program for Implementing Network Models of Multiphase Reactors",
        desc: "Technical Report, ORNL/TM-2017/748, 2018",
        url: "https://www.osti.gov/biblio/1465051"
    },
    {
        title: "Simulating Biomass Fast Pyrolysis at the Single Particle Scale",
        desc: "From the book 'Fast Pyrolysis of Biomass', Chapter 11, pp. 231-253, 2017",
        url: "http://pubs.rsc.org/en/content/chapter/bk9781782626183-00231/978-1-78801-024-5"
    },
    {
        title: "Low-Order Modeling of Internal Heat Transfer in Biomass Particle Pyrolysis",
        desc: "Energy & Fuels, 30 (6), pp. 4960-4969, 2016",
        url: "http://pubs.acs.org/doi/abs/10.1021/acs.energyfuels.6b00554"
    },
    {
        title: "Development of a Low-Order Computational Model for Biomass Fast Pyrolysis: Accounting for Particle Residence Time",
        desc: "Technical Report, ORNL/TM-2016/69, 2016",
        url: "publications/16-02-dev-low-order.pdf"
    },
    {
        title: "Coupling DAEM and CFD for simulating biomass fast pyrolysis in fluidized beds",
        desc: "Journal of Analytical and Applied Pyrolysis, 117, pp. 176-181, 2016",
        url: "http://www.sciencedirect.com/science/article/pii/S0165237015302199"
    },
    {
        title: "Biomass Particle Models with Realistic Morphology and Resolved Microstructure for Simulations of Intraparticle Transport Phenomena",
        desc: "Energy & Fuels, 29 (1), pp. 242-254, 2015",
        url: "http://pubs.acs.org/doi/abs/10.1021/ef502204v"
    },
    {
        title: "Evaluation of Biomass and Coal Briquettes for a Spreader Stoker Boiler Using an Experimental Furnace — Modeling and Test",
        desc: "Clemson University, 2011",
        url: "http://search.proquest.com/openview/a64aa7eaf57f657e66048f913355baa9/1?pq-origsite=gscholar&cbl=18750&diss=y"
    },
    {
        title: "System Modeling of ORNL's 20 MW(t) Wood-fired Gasifying Boiler",
        desc: "Conference: American Flame Research Committee, Pacific Rim Combustion Symposium, 2010",
        url: "https://www.osti.gov/scitech/biblio/992112"
    }
]

for (var i=0, len=pubs.length; i<len; i++) {
    var pElement = document.createElement('p');
    var title = '<strong>' + pubs[i].title + '</strong>';
    var desc = pubs[i].desc;
    var url = `<a href=${pubs[i].url}>Link</a>`;
    pElement.innerHTML = `${title}. ${desc}. ${url}.`;
    document.getElementById('pubs').appendChild(pElement);
}