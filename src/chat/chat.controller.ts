// src/chat/chat.controller.ts

import { Controller, Post, Body } from '@nestjs/common';
import { ChatService } from './chat.service';
import { ChatDto } from './dto';

@Controller('chat')
export class ChatController {
  constructor(private readonly chatService: ChatService) {}


  @Post('')
  async processChat(@Body() body : ChatDto ) {
    const userInput = body.text
    return await this.chatService.processChat(userInput);
  }
}
