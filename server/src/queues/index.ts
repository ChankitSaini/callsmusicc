export default new (class {
  queues: Map<number, Array<any>> = new Map();

  push(chatId: number, item: any): number {
    const queue = this.queues.get(chatId);

    if (queue) {
      queue.push(item);
      return queue.length + 1;
    }

    this.queues.set(chatId, [item]);
    return 2;
  }

  get(chatId: number): any {
    const queue = this.queues.get(chatId);

    if (queue) {
      return queue.shift();
    }

    return undefined;
  }

  getLength(chatId: number): number {
    const queue = this.queues.get(chatId);

    if (queue) {
      return queue.length;
    }

    return 0;
  }

  getAll(chatId: number): Array<any> {
    const queue = this.queues.get(chatId);

    if (queue) {
      return queue;
    }

    return [];
  }

  clear(chatId: number) {
    this.queues.set(chatId, []);
  }
})();
