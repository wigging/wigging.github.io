---
title: Text view in SwiftUI
date: 2019-07-04
layout: note
---

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

![text-view](/assets/images/text-view.png)

See Apple's [documentation](https://developer.apple.com/documentation/swiftui/text) for more information.
