#!/usr/bin/python

### FILE
self.actionOpen.triggered.connect(lambda: self.triggeredOpenButton())
self.actionSave.triggered.connect(lambda: self.triggeredSaveButton())
self.actionRestore.triggered.connect(lambda: self.triggeredRestoreButton())
self.actionClose.triggered.connect(lambda: self.triggeredCloseButton())

### EDIT
self.actionUndo.triggered.connect(lambda: self.triggeredUndoButton())
self.actionRedo.triggered.connect(lambda: self.triggeredRedoButton())
self.actionCopy.triggered.connect(lambda: self.triggeredCopyButton())
self.actionCut.triggered.connect(lambda: self.triggeredCutButton())
self.actionPaste.triggered.connect(lambda: self.triggeredPasteButton())

### WINDOW
self.actionFilter.triggered.connect(lambda: self.triggeredFilterButton())
self.actionEditor.triggered.connect(lambda: self.triggeredEditorButton())
self.actionScript.triggered.connect(lambda: self.triggeredScriptButton())
self.actionHook.triggered.connect(lambda: self.triggeredHookButton())
self.actionComand_Line.triggered.connect(lambda: self.triggeredCommandLineButton())
self.actionHistorical_Copy.triggered.connect(lambda: self.triggeredHistoricalButton())
