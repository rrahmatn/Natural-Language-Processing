import { ChatService } from './chat.service';
import { ChatDto } from './dto';
export declare class ChatController {
    private readonly chatService;
    constructor(chatService: ChatService);
    processChat(body: ChatDto): Promise<{
        chat: any[];
    }>;
}
