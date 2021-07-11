import { Router } from "express";

import pause from "./pause";
import resume from "./resume";
import stop from "./stop";
import stream from "./stream";
import leave from "./leave";

const router = Router();

router.use(pause);
router.use(resume);
router.use(stop);
router.use(stream);
router.use(leave);

export default router;
