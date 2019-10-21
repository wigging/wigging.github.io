---
title: Swift programming for macOS
date: 2019-10-20
layout: note
---

The [swift-macos](https://github.com/wigging/swift-macos) repository contains example code for the sections discussed below.

**Contents**

- [Text](#text)
- [Window size](#window-size)

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
