import { Router } from "express";

import gramtgcalls from "../../../client/gramtgcalls";
import ffmpeg from "../../../ffmpeg";
import queues from "../../../queues";

const router = Router();

export const getOnFinish = (chatId: number) => async () => {
    if (!gramtgcalls.connected(chatId)) {
        return;
    }

    const item = queues.get(chatId);

    if (item && item.filePath) {
        await gramtgcalls.stream(chatId, await ffmpeg(item.filePath), {
            onFinish: getOnFinish(chatId),
        });
        return;
    }

    await gramtgcalls.leave(chatId);
};

router.get("/stream", async (req, res) => {
    const chatId = Number(req.query.chatId);

    if (chatId && req.query.filePath) {
        const filePath = String(req.query.filePath);

        if (gramtgcalls.finished(chatId) != false) {
            try {
                await gramtgcalls.stream(chatId, await ffmpeg(filePath), {
                    onFinish: getOnFinish(chatId),
                });
            } catch (e) {
                res.json({ ok: false, result: String(e) });
                return;
            }

            res.json({ ok: true, result: null });
            return;
        }

        res.json({ ok: true, result: queues.push(chatId, { filePath }) });
        return;
    }

    res.json({ ok: false, result: false });
});

export default router;
