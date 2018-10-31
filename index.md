---
layout: default
---

Gavin Wiggins is a research scientist at the Oak Ridge National Laboratory near
Knoxville, TN. His current work is developing computational models to simulate
the fast pyrolysis of biomass in fluidized reactors. This research is part of
the [Consortium for Computational Physics and Chemistry][ccpc] for the U.S. DOE
Bioenergy Technologies Office. Gavin is also involved in various battery
simulation activities as part of the [Computer Aided Engineering for
Batteries][caebat] project. As an enthusiastic developer, he is the organizer of
the [Knoxville CocoaHeads][cocoa] and [KnoxPy][kpy] programming groups.

Get in touch: <a href = "mailto:wiggingATmeDOTcom" onclick = "this.href=this.href.replace(/AT/,'&#64;').replace(/DOT/,'&#46;')">Email</a>, [GitHub][git], [Reddit][red], [Stack Overflow][so], [Twitter][tw]

## Apps

[WeathrClip][wc] provides current weather conditions, 5-day forecast, hourly
forecast, and precipitation radar for your Mac and iPhone.

[Un1ts][un] is a comprehensive unit converter for the Mac. It was previously
available on the Mac App Store but is now open-source software.

## Code

See my [GitHub][] profile for examples of my iOS, macOS, Swift and Python code.
Organizations on GitHub that I contribute to are the [Knoxville CocoaHeads][],
[CCPC][], [KnoxPy][], [BatterySim][], [Fluidization][], and [Chemics][].

[GitHub]: https://github.com/wigging
[Knoxville CocoaHeads]: https://github.com/knoxcocoa
[CCPC]: https://github.com/ccpcode
[KnoxPy]: https://github.com/knoxpy
[BatterySim]: https://github.com/batterysim
[Fluidization]: https://github.com/fluidization
[Chemics]: https://github.com/chemics

## Presentations

{% for pres in site.data.presentations %}
<p><a href="{{ pres.link }}">{{ pres.title }}</a>. {{ pres.desc }}.</p>
{% endfor %}

## Publications

If you do not have access to a publication, please contact me and I will be genuinely delighted to send you a copy of the manuscript.

{% for pub in site.data.publications %}
<p><a href="{{ pub.link }}">{{ pub.title }}</a>. {{ pub.desc }}.</p>
{% endfor %}

[ccpc]: http://cpcbiomass.org
[caebat]: http://batterysim.org
[cocoa]: http://knoxcocoa.org
[kpy]: http://knoxpy.org
[git]: https://github.com/wigging
[red]: https://www.reddit.com/user/wiggitt
[so]: https://stackoverflow.com/users/1084875/wigging
[tw]: https://twitter.com/wigging
[wc]: http://weathrclip.com
[un]: https://github.com/wigging/un1ts-mac-app
