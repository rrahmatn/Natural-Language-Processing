import { Injectable } from "@nestjs/common";
import { PythonShell, Options } from "python-shell";

@Injectable()
export class ChatService {
  async processChat(userInput: string) {
    const pythonOptions: Options = {
      mode: "text",
      scriptPath: "src/model/chatbot",
      args: [userInput],
    };

    const response = await PythonShell.run("chat.py", pythonOptions)

    return {
        chat : response
    }
  }
}
