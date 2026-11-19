// Entry for make.fun's "Sum up 18 November's world news in one image" bounty (Node 22, standard library only).
// The picture itself is entry.png beside this file: a one-page summary of Wednesday 18 November 2026 — the
// Shenzhen APEC meeting of Xi and Putin with Trump arriving, Ukraine's second-night strike on the Kerch Bridge,
// the ship attack in the Strait of Hormuz, Mary Peltola's Alaska Senate win, Gaza's winter warning for 950,000
// displaced people, and Nvidia/COP31 in markets and climate. build_image.py is the script that drew it.
//
// This program copies entry.png to /output/entry.png, byte for byte, so both grader runs write identical
// bytes. The gate takes a whole PNG or JPEG of at most 1 MiB and 1024 by 1024 pixels, and the judge sees
// exactly the bytes copied.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const sourceImage = new URL('./entry.png', import.meta.url);
mkdirSync(outputDir, { recursive: true });
copyFileSync(sourceImage, join(outputDir, 'entry.png'));
