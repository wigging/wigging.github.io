# Personal Website

Repository for my peronsal website [https://gavinw.me](https://gavinw.me).

## Installation and Usage

The site is built with Jekyll using the GitHub Pages gem. Bundler is used for the Ruby environment.

Install Bundler per the instructions at [bundler.io](https://bundler.io) such as:

```bash
$ gem install bundler
```

Next, create a GitHub Pages Gemfile by following the instructions at [github.com/github/pages-gem](https://github.com/github/pages-gem):

```bash
source 'https://rubygems.org'
gem 'github-pages', group: :jekyll_plugins
```

Create the Ruby environment for the project:

```bash
$ bundle install
```

Run the Jekyll server as follows:

```bash
$ bundle exec jekyll serve
```

## Updating

```bash
# Update the Ruby Bundler gem
$ gem update bundler

# Update the GitHub Pages gem
$ bundle update github-pages
```

## Further Reading

- Bundler https://bundler.io
- GitHub Pages Ruby Gem https://github.com/github/pages-gem
- Jekyll https://jekyllrb.com
