### Note:
This is the documentation for https://github.com/mixxxdj/mixxx/pull/1346. Unfortunately that PR went stale, ie. the mapping is not included in any Mixxx release, yet. You can still use this mapping by downloading the xml and js files from that PR's "Files changed" tab.
If you plan to adopt that PR in order to get the mapping included finally, please comment there.


# Pioneer-DDJ-WeGO

<https://www.pioneerelectronics.com/PUSA/DJ/Controllers/DDJ-WeGO>

| ![ ![](../../_static/controllers/pioneerddjwego/pioneer-ddj-wego-top.png](pioneerddjwego/pioneer-ddj-wego-left.png) ) | ![](pioneerddjwego/pioneer-ddj-wego-right.png) |
| ------------------------------------------------------- | ------------------------------------------------------ | -------------------------------------------------------- |
|                                                         | ![](pioneerddjwego/pioneer-ddj-wego-lit.png) |                                                          |

## Mapping Description

Built and tested with mixxx 2.0.0 (build 1.12 r5772) My goal with the
mapping is to be as close to the behaviour of Pioneers original
intention with the device demoed in their marketing material.

### Compromises:

  - Auto loop buttons default to creating a loop of 32.
  - FX\[123\] buttons turn on the effected channels of EffectUnit\[123\]
  - \[shift\] FX\[123\] cycle the EffectUnit\[123\]'s effect type.
  - FX jogwheels and \[shift\]jogwheels effect the mix and super1 of the
    EffectUnit\[123\].
  - ctrlB controls the QuickEffectsRack1\_\[Channeln\]\_Effect1\]

### What works:

  - Deck switching for 4 decks
  - Cue, play hotcue\[1-4\], volume, \[low|med|high\]eq knobs, headphone
    cue, browse, load, autoloop, tempo, sampler\[1-4\], sync\_master
  - Scratching
  - Lighting effects for ctrlA, ctrlB and fx buttons, with script option
    to turn them off.
  - ctrlA controls pitch, ctrlB controls QuickEffectsRack1
