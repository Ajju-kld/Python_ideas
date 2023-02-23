import 'package:flutter/material.dart';
import 'package:openai/openai.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'GPT-3 Chat App',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: ChatScreen(),
    );
  }
}

class ChatScreen extends StatefulWidget {
  @override
  _ChatScreenState createState() => _ChatScreenState();
}

class _ChatScreenState extends State<ChatScreen> {
  final textController = TextEditingController();
  final messages = <String>[];

  Future<void> handleResponse(String prompt) async {
    final response = await Openai.complete(model: "text-davinci-002", prompt: prompt);
    setState(() {
      messages.add('Bot: ${response.choices[0].text}');
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('GPT-3 Chat App'),
      ),
      body: Column(
        children: [
          Expanded(
            child: ListView.builder(
              itemCount: messages.length,
              itemBuilder: (context, index) => Text(messages[index]),
            ),
          ),
          TextField(
            controller: textController,
            onSubmitted: (text) async {
              textController.clear();
              setState(() {
                messages.add('You: $text');
              });
              await handleResponse(text);
            },
          ),
        ],
      ),
    );
  }
}
