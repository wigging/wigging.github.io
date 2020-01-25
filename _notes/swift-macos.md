---
title: Swift programming for macOS
desc: Notes and example code for developing Mac apps in Swift
date: 2020-01-24
layout: note
---

There are plenty of books, videos, and online resources for developing iOS, tvOS, watchOS, and iPadOS apps. Despite the fact that all of these platforms require a Mac for code development, there is very little information about actually creating native Mac applications. The examples given below demonstrate various aspects of Mac app development and will hopefully provide a useful resource for developers.

See the [swift-macos](https://github.com/wigging/swift-macos) repository for example code.

**Contents**

- [Picker control](#picker-control)
- [Preferences window](#preferences-window)
- [Sidebar navigation](#sidebar-navigation)
- [Stepper control](#stepper-control)
- [Text field](#text-field)
- [Text view](#text-view)
- [Web view](#web-view)
- [Window size](#window-size)

## Picker control

The picker control selects an item from a set of values. The appearance of the picker can be changed with the available styles and label modifier.

![picker](/assets/images/picker.png)

```swift
import SwiftUI

struct ContentView: View {

    let bands = ["Nirvana", "Pearl Jam", "NIN"]
    @State private var selectedBand = 0

    @State private var selectedName = 0

    var body: some View {
        VStack(spacing: 20) {

            Picker("Band", selection: $selectedBand) {
                ForEach(0..<bands.count) {
                    Text(self.bands[$0])
                }
            }

            Picker("Band", selection: $selectedBand) {
                ForEach(0..<bands.count) {
                    Text(self.bands[$0])
                }
            }
            .pickerStyle(RadioGroupPickerStyle())

            Picker("Band", selection: $selectedBand) {
                ForEach(0..<bands.count) {
                    Text(self.bands[$0])
                }
            }
            .pickerStyle(SegmentedPickerStyle())

            Picker("Name", selection: $selectedName) {
                Text("Homer Simpson").tag(0)
                Text("Lisa Simpson").tag(1)
                Text("Bart Simpson").tag(2)
            }
            .fixedSize()

            Picker("Name", selection: $selectedName) {
                Text("Homer Simpson").tag(0)
                Text("Lisa Simpson").tag(1)
                Text("Bart Simpson").tag(2)
            }
            .labelsHidden()
            .fixedSize()

        }
        .padding()
        .frame(width: 400, height: 300)
    }
}
```

## Preferences window

A preferences window contains user settings for the application. This window is usually opened from the Preferences item in the application's menu bar. To open a window from the Preferences menu item, connect an IBAction between the item and AppDelegate.

![preferences menu](/assets/images/preferences-menu.png){: .large-img}

```swift
// AppDelegate.swift

@NSApplicationMain
class AppDelegate: NSObject, NSApplicationDelegate {

    var prefsWindow: NSWindow!

    @IBAction func openPrefsWindow(_ sender: NSMenuItem) {
        let prefsView = PreferencesView()
        prefsWindow = NSWindow(
            contentRect: NSRect(x: 0, y: 0, width: 480, height: 300),
            styleMask: [.titled, .closable],
            backing: .buffered,
            defer: false)
        prefsWindow.center()
        prefsWindow.title = "Preferences"
        prefsWindow.setFrameAutosaveName("Preferences Window")
        prefsWindow.contentView = NSHostingView(rootView: prefsView)
        prefsWindow.makeKeyAndOrderFront(nil)
        prefsWindow.isReleasedWhenClosed = false
    }

    // other code
}
```

The contents of the Preferences window is defined in a separate file where controls, text, and other items are added to the window's view.

![preferences window](/assets/images/preferences-window.png)

```swift
// PreferencesView.swift

import SwiftUI

struct PreferencesView: View {
    var body: some View {
        Text("My Preferences Window")
            .font(.headline)
            .frame(width: 400, height: 200)
    }
}

struct PreferencesView_Previews: PreviewProvider {
    static var previews: some View {
        PreferencesView()
    }
}
```

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

## Stepper control

The stepper control increments and decrements a value. A closed range can be used to limit the applicable stepper values.

![stepper](/assets/images/stepper.png)

```swift
import SwiftUI

struct ContentView: View {

    @State private var age = 18
    @State private var hours = 4.0
    @State private var number = 1
    @State private var setting = UserDefaults.standard.integer(forKey: "Setting")

    var body: some View {
        VStack(spacing: 20) {

            Stepper("Age: \(age)", value: $age, in: 10...20)
                .frame(width: 120, alignment: .trailing)

            Stepper("Hours: \(hours, specifier: "%g")", value: $hours, in: 1...10, step: 0.25)
                .frame(width: 120, alignment: .trailing)

            Stepper("Number: \(number)", onIncrement: {
                print("on increment")
                self.number += 1
            }, onDecrement: {
                print("on decrement")
                self.number -= 1
            })
                .frame(width: 120, alignment: .trailing)

            Stepper("Another Number: \(number)", onIncrement: {
                print("on increment")
                self.number += 1
            }, onDecrement: {
                print("on decrement")
                self.number -= 1
            }, onEditingChanged: { edited in
                if edited {
                    print("edited")
                } else {
                    print("not edited")
                }
            })
                .frame(width: 180, alignment: .trailing)

            Stepper("Setting: \(setting)", value: $setting, in: 0...5, onEditingChanged: { _ in
                UserDefaults.standard.set(self.setting, forKey: "Setting")
            })
                .frame(width: 120, alignment: .trailing)

        }
        .frame(width: 400, height: 220)
    }
}
```

## Text field

The `TextField` structure is a control that provides an editable text field. Various modifiers are available to customize the appearance and text alignment. Actions can be performed when editing begins and ends for the text field or when the return key is pressed.

![text field](/assets/images/text-field.png)

```swift
import SwiftUI

struct ContentView: View {
    @State private var text1 = ""

    var body: some View {
        VStack {
            TextField("Example 1", text: $text1)

            TextField("Example 2", text: $text1)
                .fixedSize()

            TextField("Example 3", text: $text1)
                .textFieldStyle(RoundedBorderTextFieldStyle())

            TextField("Example 4", text: $text1)
                .multilineTextAlignment(.center)

            TextField("Example 5", text: $text1)
                .multilineTextAlignment(.trailing)

            TextField("Example 6", text: $text1)
                .foregroundColor(.red)

            TextField("Example 7", text: $text1, onEditingChanged: { editing in
                if editing {
                    print("is editing")
                } else {
                    print("not editing")
                }
            })

            TextField("Example 8", text: $text1) {
                print("on commit")
            }

        }
        .padding()
        .frame(width: 480, height: 300)
    }
}
```

## Text view

The `Text` structure in SwiftUI is a view that displays lines of text. Various modifiers are available to customize the appearance and style of text.

![text view](/assets/images/text-view.png)

```swift
import SwiftUI

struct ContentView: View {
    var body: some View {
         VStack {
            Text("Hello World")
            Text("Hello World").bold()
            Text("Hello World").italic()
            Text("Hello World").foregroundColor(.red)
            Text("Hello World").fontWeight(.ultraLight)
            Text("Hello World").underline()
            Text("Hello World").underline(true, color: .red)
            Text("Hello World").strikethrough()
            Text("Hello World").strikethrough(true, color: .green)
            Text("Hello > ").foregroundColor(.green) + Text("World").foregroundColor(.blue)
         }
         .frame(width: 400, height: 300)
    }
}
```

## Web view

A WKWebView from the WebKit framework is used to display web content in a window. The web view can be wrapped with NSViewRepresentable to make it usable with SwiftUI. Content for the web view can be loaded using a website url, a string representing HTML content, or by loading an HTML file.

```swift
import SwiftUI
import WebKit

// A view representing a WKWebView for displaying a webpage using a url.

struct WebView: NSViewRepresentable {

    let url: String

    func makeNSView(context: Context) -> WKWebView {

        guard let url = URL(string: self.url) else {
            return WKWebView()
        }

        let webview = WKWebView()
        let request = URLRequest(url: url)
        webview.load(request)
        return webview
    }

    func updateNSView(_ nsView: WKWebView, context: Context) { }
}
```

```swift
// A view representing a WKWebView for displaying HTML content.

struct WebView: NSViewRepresentable {

    let content: String

    func makeNSView(context: Context) -> WKWebView {

        let webview = WKWebView()
        webview.loadHTMLString(self.content, baseURL: nil)
        return webview
    }

    func updateNSView(_ nsView: WKWebView, context: Context) { }
}
```

```swift
// A view representing a WKWebView for displaying an HTML file.

struct WebView: NSViewRepresentable {

    let file: String

    func makeNSView(context: Context) -> WKWebView {

        guard let url = Bundle.main.url(forResource: self.file, withExtension: "html") else {
            return WKWebView()
        }

        let webview = WKWebView()
        webview.loadFileURL(url, allowingReadAccessTo: url)
        return webview
    }

    func updateNSView(_ nsView: WKWebView, context: Context) { }
}
```

For SwiftUI to properly display the WebView, it must be within a GeometryReader and ScrollView.

```swift
import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack {
            GeometryReader { geom in
                ScrollView {
                    WebView(url: "https://www.apple.com")
                        .frame(height: geom.size.height)
                }
            }
            Text("Apple's website")
        }
        .padding()
        .frame(width: 480, height: 600)
    }
}
```

## Window size

The window size is defined by the frame size of the containing view. In this example the VStack frame is set to a width of 500 and height of 300 which makes the window width 500 and height 300.

![window size](/assets/images/window-size.png)

```swift
import SwiftUI

struct ContentView : View {
    var body: some View {
        VStack {
            Text("Hello World")
        }
        .frame(width: 500, height: 300)
    }
}
```
