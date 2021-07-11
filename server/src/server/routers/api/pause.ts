import { Router } from "express";
import gramtgcalls from "../../../client/gramtgcalls";

const router = Router();

router.get("/pause", (req, res) => {
    const chatId = Number(req.query.chatId);

    if (chatId) {
        res.json({
            ok: true,
            result: gramtgcalls.pause(Number(req.query.chatId)),
        });
        return;
    }

    res.json({ ok: false, result: false });
});

export default router;
