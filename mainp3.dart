import 'package:flutter/material.dart';

void main() => runApp(SignViewerApp());

class SignViewerApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Traffic Sign Viewer',
      home: Scaffold(
        appBar: AppBar(title: Text('Detected Signs')),
        body: SignDisplay(),
      ),
    );
  }
}

class SignDisplay extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // Replace this with actual camera feed or REST API results
    final detectedSigns = [
      {'label': 'Stop', 'timestamp': '10:42:01'},
      {'label': 'Yield', 'timestamp': '10:43:22'},
    ];

    return ListView.builder(
      itemCount: detectedSigns.length,
      itemBuilder: (context, index) {
        final sign = detectedSigns[index];
        return ListTile(
          leading: Icon(Icons.traffic),
          title: Text(sign['label']!),
          subtitle: Text("Detected at ${sign['timestamp']}"),
        );
      },
    );
  }
}

