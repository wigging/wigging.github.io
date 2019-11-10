---
title: Swift programming for macOS
date: 2019-11-10
layout: note
---

See the [swift-macos](https://github.com/wigging/swift-macos) repository for example code.

**Contents**

- [Sidebar navigation](#sidebar-navigation)
- [Text](#text)
- [Window size](#window-size)

## Sidebar navigation

A navigation view contains a sidebar and detail view. Selecting an item in the sidebar will change the detail view accordingly. The selection binding for the list view must be implemented otherwise items will not be selectable when the app launches.

![sidebar](/assets/images/sidebar.png)

```swift
// ContentView.swift

import SwiftUI

struct SidebarView: View {

    // This binding must be implemented with List otherwise item selection
    // will not work properly when the app launches.
    @State private var selected = Set<String>()

    private let items = ["🍎 Apple", "🍌 Banana", "🥥 Coconut", "🍒 Cherry", "🥜 Peanut", "🍑 Peach", "🍅 Tomato", "🍞 Bread", "🍕 Pizza", "🥦 Broccoli", "🥝 Kiwi", "🧀 Cheese", "🍉 Watermelon"]

    var body: some View {
        List(items, id: \.self, selection: $selected) { item in
            NavigationLink(destination: DetailView(selection: item)) {
                Text("\(item)")
            }
        }
        .listStyle(SidebarListStyle())
    }
}

struct DetailView: View {

    var selection: String

    var body: some View {
        switch selection {
        case "🍎 Apple":
            return AnyView(AppleView())
        case "🍌 Banana":
            return AnyView(BananaView())
        case "🥥 Coconut":
            return AnyView(CoconutView())
        default:
            return AnyView(
                Text("Some \(selection) view here")
                    .frame(maxWidth: .infinity, maxHeight: .infinity)
            )
        }
    }
}

struct ContentView: View {
    var body: some View {
        NavigationView {
            SidebarView()
            DetailView(selection: "🍎 Apple")
        }
        .frame(height: 300)
    }
}
```

Detail views are defined in separate files such as the apple view shown below.

```swift
// AppleView.swift

import SwiftUI

struct AppleView: View {
    var body: some View {
        VStack(spacing: 10) {
            Text("Hello from")
                .font(.title)
            Text("🍎 Apple View")
                .font(.largeTitle)
        }
        .frame(width: 480, height: 300)
    }
}
```

## Text

The `Text` structure in SwiftUI is a view that displays lines of text. Various modifiers are available to customize the appearance and style of text.

```swift
Text("Hello World")
Text("Hello World").bold()
Text("Hello World").italic()
Text("Hello World").color(.red)
Text("Hello World").fontWeight(.ultraLight)
Text("Hello World").underline()
Text("Hello World").underline(true, color: .red)
Text("Hello World").strikethrough()
Text("Hello World").strikethrough(true, color: .green)
```

![text view](/assets/images/text-view.png)

## Window size

The window size can be defined by setting the frame size of the containing view. In this example the VStack frame is set to a width of 500 and height of 300; therefore, the window will size will be 500 by 300.

```swift
struct ContentView : View {
    var body: some View {
        VStack {
            Text("Hello World")
        }
        .frame(width: 500, height: 300)
    }
}
```

![window size](/assets/images/window-size.png)
