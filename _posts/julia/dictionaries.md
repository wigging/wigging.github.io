---
title: Dictionaries in Julia
date: May 22, 2021
---

The `Dict()` constructor is used to create dictionaries in Julia. A dictionary is constructed using key value pairs separated with `=>` or as tuples.

```julia
# Dictionary using key => value
contacts = Dict("Bart" => 14, "Marge" => 39, "Homer" => 44)

# Dictionary using (key, value)
contacts2 = Dict([("Lisa", 16), ("Krusty", 28)])
```
