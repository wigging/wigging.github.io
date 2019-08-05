---
title: Exponential Sums
date: 2019-08-04
layout: article
---

An exponential sum is represented by the following equation

$$\sum_{n=1}^N e^{2 \pi i f(n)}$$

where the exponential is a complex number. The function $f(n)$ is a real-valued function defined for a sequence of positive integers. The exponential sum can be plotted in the complex plane as a progression of partial sums. The x-axis on the plot is the real part and the y-axis is the imaginary part.

## Python package

The Python package `expsum` is a command line tool to plot and optionally animate the exponential sum for a specific function. See the [exponential-sums](https://github.com/wigging/exponential-sums) repository on GitHub for installation and usage instructions. Examples of using the `expsum` tool for various functions are shown below. An animated plot can be displayed using the optional `--anim` argument. See the GitHub repo for more details.

## Function 1

$$f(n) = \frac{n}{a} + \frac{n^2}{b} + \frac{n^3}{c}$$

```bash
>>> python expsum func1 2000 10 7 17
```

![func1a plot](/assets/images/func1a.pdf){: .center-image }

```bash
>>> python expsum func1 8000 11 21 31
```

![func1b plot](/assets/images/func1b.pdf){: .center-image }

## Function 2

$$f(n) = \log(n) + \frac{n^2}{a}$$

```bash
>>> python expsum func2 1200 100
```

![func2a plot](/assets/images/func2a.pdf){: .center-image }

```bash
>>> python expsum func2 4000 800
```

![func2b plot](/assets/images/func2b.pdf){: .center-image }

## Function 3

$$f(n) = \log(n)^{4.1}$$

```bash
>>> python expsum func3 1000
```

![func3a plot](/assets/images/func3a.pdf){: .center-image }

```bash
>>> python expsum func3 4000
```

![func3b plot](/assets/images/func3b.pdf){: .center-image }

## Function 4

$$f(n) = (\log(n))^a$$

```bash
>>> python expsum func4 4000 4
```

![func4a plot](/assets/images/func4a.pdf){: .center-image }

## Function 5

$$f(n) = \log(n) + \frac{n^2}{a} + \frac{n^3}{b}$$

```bash
>>> python expsum func5 4000 50 100
```

![func5a plot](/assets/images/func5a.pdf){: .center-image }

## Function 6

$$f(n) = \frac{\sqrt n}{a}$$

```bash
>>> python expsum func6 2000 4
```

![func6a plot](/assets/images/func6a.pdf){: .center-image }

## Function 7

$$f(n) = \frac{\sqrt{n^3}}{a}$$

```bash
>>> python expsum func7 8000 4
```

![func7a plot](/assets/images/func7a.pdf){: .center-image }

## References

This article was inspired by John Cook's blog post "Exponential sums make pretty pictures".

1. John D. Cook. [Exponential sums make pretty pictures][1]. October 7, 2017.
2. David Angell. [Exponential sums][2]. School of Mathematics and Statistics, UNSW. Accessed July 7, 2019.
3. Wikipedia contributors. [Exponential sum][3]. In Wikipedia, The Free Encyclopedia. Accessed July 20, 2019.

[1]: https://www.johndcook.com/blog/2017/10/07/exponential-sums-make-pretty-pictures/
[2]: https://www.maths.unsw.edu.au/about/exponential-sums
[3]: https://en.wikipedia.org/wiki/Exponential_sum
