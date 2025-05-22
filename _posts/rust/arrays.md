---
title: Arrays in Rust
date: November 14, 2022
---

An array is a collection of values where every element must have the same type. The length of an array is fixed and the first item is at index 0.

```rust
// Create an array of integers and access the first item
let a = [3, 4, 5, 6, 7, 8];
let first_item = a[0];

println!("First item in a is {first_item}");
// First item in a is 3
```

```rust
// Create an array with 3 elements of i64 and get the second item
let b: [i64; 3] = [12, 8, 5];
let second_item = b[1];

println!("Second item in b is {second_item}");
// Second item in b is 8
```

```rust
// Create an array of 4 elements where each element is 1
let c = [1; 4];

println!("The c array is {:?}", c);
// The c array is [1, 1, 1, 1]
```

```rust
// Get the length (number of elements) of an array
let d = [3, 4, 5, 6, 7];
let length_of_d = d.len();

println!("Length of d is {length_of_d}");
// Length of d is 5
```
