# N.B.: MusicXML uses long instead of longa

```Python
typeToDuration: t.Dict[str, float] = {
'duplex-maxima': 64.0,
'maxima': 32.0,
'longa': 16.0,
'breve': 8.0,
'whole': 4.0,
'half': 2.0,
'quarter': 1.0,
'eighth': 0.5,
'16th': 0.25,
'32nd': 0.125,
'64th': 0.0625,
'128th': 0.03125,
'256th': 0.015625,
'512th': 0.015625 / 2.0,
'1024th': 0.015625 / 4.0,
'2048th': 0.015625 / 8.0,
'zero': 0.0,
}
```
