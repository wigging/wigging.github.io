---
title: Swift programming for macOS
---

There are plenty of books, videos, and online resources for developing iOS apps. Despite the fact that iPhone and iPad apps require a Mac for code development, there is very little information about actually creating native Mac applications. The examples in this post demonstrate various aspects of Mac app development and will hopefully provide a useful resource for developers.

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

A navigation view contains a master and detail view. In this example, the master view displays a list of fruits in the sidebar. The detail view determines which view to display based on which item is selected in the sidebar.

![sidebar](/assets/images/sidebar.png)

The content view of the window is a navigation view that contains the master and detail views. An enum defines the state of the sidebar list selection and is used to determine which view is displayed by the detail view. UserDefaults stores the selection so that the detail view displays the last viewed item when the app is relaunched.

```swift
// ContentView.swift

import SwiftUI

struct ContentView: View {

    @State private var selectedFruit: Fruit?

    var body: some View {
        NavigationView {
            NavigationMaster(selectedFruit: $selectedFruit)
            NavigationDetail(fruit: $selectedFruit)
        }
    }
}

// NavigationMaster.swift

struct NavigationMaster: View {

    @Binding var selectedFruit: Fruit?
    private let defaultFruit = Fruit(rawValue: UserDefaults.standard.object(forKey: "SelectedFruit") as? String ?? "🥭 Mango")

    var body: some View {
        List(Fruit.allCases, id: \.self, selection: $selectedFruit) { fruit in
            Text("\(fruit.rawValue)")
        }
        .listStyle(SidebarListStyle())
        .onAppear {
            self.selectedFruit = self.defaultFruit
        }
    }
}

// NavigationDetail.swift

struct NavigationDetail: View {

    @Binding var fruit: Fruit?

    var body: some View {

        switch fruit {
        case .apple:
            UserDefaults.standard.set(Fruit.apple.rawValue, forKey: "SelectedFruit")
            return AnyView(AppleView())
        case .coconut:
            UserDefaults.standard.set(Fruit.coconut.rawValue, forKey: "SelectedFruit")
            return AnyView(CoconutView())
        case .mango:
            UserDefaults.standard.set(Fruit.mango.rawValue, forKey: "SelectedFruit")
            return AnyView(MangoView())
        case .kiwi:
            UserDefaults.standard.set(Fruit.kiwi.rawValue, forKey: "SelectedFruit")
            return AnyView(KiwiView())
        case .none:
            return AnyView(Text("Default View").frame(width: 300, height: 200))
        }
    }
}

// Fruit.swift

enum Fruit: String, CaseIterable {
    case apple = "🍎 Apple"
    case coconut = "🥥 Coconut"
    case mango = "🥭 Mango"
    case kiwi = "🥝 Kiwi"
}
```

To properly render the entire navigation view in the window, the frame is specified for each detail view. Note that each detail view is the same size. If the views are different sizes the window will try to adjust its size accordingly. Unfortunately, macOS windows animating size changes with SwiftUI is buggy so in this example I use a scroll view for large detail views.

```swift
// AppleView.swift

struct AppleView: View {
    var body: some View {
        VStack {
            Text("Apple View").font(.largeTitle)
            Text("🍎").font(.title)
        }
        .frame(width: 300, height: 200)
    }
}

// CoconutView.swift

struct CoconutView: View {
    var body: some View {
        VStack {
            Text("Coconut View").font(.largeTitle)
            Text("🥥").font(.title)
        }
        .frame(width: 300, height: 200)
    }
}

// Mango.swift

struct MangoView: View {
    var body: some View {
        ScrollView(.vertical) {
            VStack {
                Text("Mango View").font(.largeTitle)
                Text("🥭").font(.largeTitle)
                ForEach(1..<20) {
                    Text("Mango \($0)")
                }
            }
            .frame(width: 300)
            .padding(.vertical)
        }
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
![web view](/assets/images/web-view.png)

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
