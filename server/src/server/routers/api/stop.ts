import { Router } from "express";
import gramtgcalls from "../../../client/gramtgcalls";
import { getOnFinish } from "./stream";

const router = Router();

router.get("/stop", (req, res) => {
  const chatId = Number(req.query.chatId);

  if (chatId) {
    res.json({ ok: true, result: gramtgcalls.stop(chatId) });
    getOnFinish(chatId)();
    return;
  }

  res.json({ ok: false, result: false });
});

export default router;
