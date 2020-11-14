from typing import Tuple, Set, Iterable, List


class ThemedAboutDialogHandler:
    def __init__(self): ...
    @property
    def Copyright(self) -> str: ...
    @property
    def Designers(self) -> Set(str): ...
    @property
    def Developers(self) -> Set(str): ...
    @property
    def Documenters(self) -> Set(str): ...
    @property
    def License(self) -> str: ...
    @property
    def Logo(self) -> Image: ...
    @property
    def ProgramDescription(self) -> str: ...
    @property
    def ProgramName(self) -> str: ...
    @property
    def Title(self) -> str: ...
    @property
    def Version(self) -> str: ...
    @property
    def Website(self) -> Uri: ...
    @property
    def WebsiteLabel(self) -> str: ...
    @Copyright.setter
    def Copyright(self, value: str) -> None: ...
    @Designers.setter
    def Designers(self, value: Set(str)) -> None: ...
    @Developers.setter
    def Developers(self, value: Set(str)) -> None: ...
    @Documenters.setter
    def Documenters(self, value: Set(str)) -> None: ...
    @License.setter
    def License(self, value: str) -> None: ...
    @Logo.setter
    def Logo(self, value: Image) -> None: ...
    @ProgramDescription.setter
    def ProgramDescription(self, value: str) -> None: ...
    @ProgramName.setter
    def ProgramName(self, value: str) -> None: ...
    @Title.setter
    def Title(self, value: str) -> None: ...
    @Version.setter
    def Version(self, value: str) -> None: ...
    @Website.setter
    def Website(self, value: Uri) -> None: ...
    @WebsiteLabel.setter
    def WebsiteLabel(self, value: str) -> None: ...
    def ShowDialog(self, parent: Window) -> DialogResult: ...


class ThemedButtonSegmentedItemHandler:
    def __init__(self): ...


class ThemedCollectionEditor(Panel):
    def __init__(self): ...
    @property
    def DataStore(self) -> Iterable[Object]: ...
    @property
    def ElementType(self) -> Type: ...
    @property
    def ExtraContent(self) -> Control: ...
    @DataStore.setter
    def DataStore(self, value: Iterable[Object]) -> None: ...
    @ElementType.setter
    def ElementType(self, value: Type) -> None: ...
    @ExtraContent.setter
    def ExtraContent(self, value: Control) -> None: ...


class ThemedCollectionEditorHandler:
    def __init__(self): ...
    @property
    def DataStore(self) -> Iterable[Object]: ...
    @property
    def ElementType(self) -> Type: ...
    @DataStore.setter
    def DataStore(self, value: Iterable[Object]) -> None: ...
    @ElementType.setter
    def ElementType(self, value: Type) -> None: ...


class ThemedDocumentControlHandler:
    def __init__(self): ...
    def AttachEvent(self, id: str) -> None: ...
    @property
    def AllowReordering(self) -> bool: ...
    @property
    def Enabled(self) -> bool: ...
    @property
    def Font(self) -> Font: ...
    @property
    def SelectedIndex(self) -> int: ...
    @property
    def TabPadding(self) -> Padding: ...
    def GetPage(self, index: int) -> DocumentPage: ...
    def GetPageCount(self) -> int: ...
    def InsertPage(self, index: int, page: DocumentPage) -> None: ...
    def OnLoad(self, e: EventArgs) -> None: ...
    def RemovePage(self, index: int) -> None: ...
    @AllowReordering.setter
    def AllowReordering(self, value: bool) -> None: ...
    @Enabled.setter
    def Enabled(self, value: bool) -> None: ...
    @Font.setter
    def Font(self, value: Font) -> None: ...
    @SelectedIndex.setter
    def SelectedIndex(self, value: int) -> None: ...
    @TabPadding.setter
    def TabPadding(self, value: Padding) -> None: ...


class ThemedDocumentPageHandler:
    def __init__(self): ...
    @property
    def Closable(self) -> bool: ...
    @property
    def Content(self) -> Control: ...
    @property
    def ContextMenu(self) -> ContextMenu: ...
    @property
    def Image(self) -> Image: ...
    @property
    def MinimumSize(self) -> Size: ...
    @property
    def Padding(self) -> Padding: ...
    @property
    def PropagateLoadEvents(self) -> bool: ...
    @property
    def Text(self) -> str: ...
    @Closable.setter
    def Closable(self, value: bool) -> None: ...
    @Content.setter
    def Content(self, value: Control) -> None: ...
    @ContextMenu.setter
    def ContextMenu(self, value: ContextMenu) -> None: ...
    @Image.setter
    def Image(self, value: Image) -> None: ...
    @MinimumSize.setter
    def MinimumSize(self, value: Size) -> None: ...
    @Padding.setter
    def Padding(self, value: Padding) -> None: ...
    @Text.setter
    def Text(self, value: str) -> None: ...


class ThemedExpanderHandler:
    def __init__(self): ...
    def AttachEvent(self, id: str) -> None: ...
    @property
    def CollapsedButtonText(self) -> str: ...
    @property
    def Content(self) -> Control: ...
    @property
    def ContextMenu(self) -> ContextMenu: ...
    @property
    def Expanded(self) -> bool: ...
    @property
    def ExpandedButtonText(self) -> str: ...
    @property
    def Header(self) -> Control: ...
    @property
    def MinimumSize(self) -> Size: ...
    @property
    def Padding(self) -> Padding: ...
    @CollapsedButtonText.setter
    def CollapsedButtonText(self, value: str) -> None: ...
    @Content.setter
    def Content(self, value: Control) -> None: ...
    @ContextMenu.setter
    def ContextMenu(self, value: ContextMenu) -> None: ...
    @Expanded.setter
    def Expanded(self, value: bool) -> None: ...
    @ExpandedButtonText.setter
    def ExpandedButtonText(self, value: str) -> None: ...
    @Header.setter
    def Header(self, value: Control) -> None: ...
    @MinimumSize.setter
    def MinimumSize(self, value: Size) -> None: ...
    @Padding.setter
    def Padding(self, value: Padding) -> None: ...


class ThemedFilePickerHandler:
    def __init__(self): ...
    def AttachEvent(self, id: str) -> None: ...
    def ClearFilters(self) -> None: ...
    @property
    def CurrentFilterIndex(self) -> int: ...
    @property
    def FileAction(self) -> FileAction: ...
    @property
    def FilePath(self) -> str: ...
    @property
    def Title(self) -> str: ...
    def InsertFilter(self, index: int, filter: FileFilter) -> None: ...
    def RemoveFilter(self, index: int) -> None: ...
    @CurrentFilterIndex.setter
    def CurrentFilterIndex(self, value: int) -> None: ...
    @FileAction.setter
    def FileAction(self, value: FileAction) -> None: ...
    @FilePath.setter
    def FilePath(self, value: str) -> None: ...
    @Title.setter
    def Title(self, value: str) -> None: ...


class ThemedFontPickerHandler:
    def __init__(self): ...
    def AttachEvent(self, id: str) -> None: ...
    @property
    def Value(self) -> Font: ...
    @Value.setter
    def Value(self, value: Font) -> None: ...


class ThemedMenuSegmentedItemHandler:
    def __init__(self): ...
    @property
    def CanSelect(self) -> bool: ...
    @property
    def Menu(self) -> ContextMenu: ...
    @property
    def MenuDelay(self) -> TimeSpan: ...
    @property
    def MenuIndicator(self) -> str: ...
    @property
    def Text(self) -> str: ...
    @CanSelect.setter
    def CanSelect(self, value: bool) -> None: ...
    @Menu.setter
    def Menu(self, value: ContextMenu) -> None: ...
    @MenuDelay.setter
    def MenuDelay(self, value: TimeSpan) -> None: ...
    @MenuIndicator.setter
    def MenuIndicator(self, value: str) -> None: ...
    @Text.setter
    def Text(self, value: str) -> None: ...


class ThemedPropertyGrid(Panel):
    def __init__(self): ...
    def add_PropertyValueChanged(self, value: EventHandler) -> None: ...
    def add_ShowCategoriesChanged(self, value: EventHandler) -> None: ...
    def CreateCellValueBinding(self) -> IndirectBinding: ...
    @property
    def PropertyCellTypes(self) -> List[PropertyCellType]: ...
    @property
    def SelectedObject(self) -> Object: ...
    @property
    def SelectedObjects(self) -> Iterable[Object]: ...
    @property
    def ShowCategories(self) -> bool: ...
    @property
    def ShowDescription(self) -> bool: ...
    @property
    def UseValueTypeDefaults(self) -> bool: ...
    def Refresh(self) -> None: ...
    def remove_PropertyValueChanged(self, value: EventHandler) -> None: ...
    def remove_ShowCategoriesChanged(self, value: EventHandler) -> None: ...
    @SelectedObject.setter
    def SelectedObject(self, value: Object) -> None: ...
    @SelectedObjects.setter
    def SelectedObjects(self, value: Iterable[Object]) -> None: ...
    @ShowCategories.setter
    def ShowCategories(self, value: bool) -> None: ...
    @ShowDescription.setter
    def ShowDescription(self, value: bool) -> None: ...
    @UseValueTypeDefaults.setter
    def UseValueTypeDefaults(self, value: bool) -> None: ...


class ThemedPropertyGridHandler:
    def __init__(self): ...
    def AttachEvent(self, id: str) -> None: ...
    @property
    def SelectedObject(self) -> Object: ...
    @property
    def SelectedObjects(self) -> Iterable[Object]: ...
    @property
    def ShowCategories(self) -> bool: ...
    @property
    def ShowDescription(self) -> bool: ...
    def Refresh(self) -> None: ...
    @SelectedObject.setter
    def SelectedObject(self, value: Object) -> None: ...
    @SelectedObjects.setter
    def SelectedObjects(self, value: Iterable[Object]) -> None: ...
    @ShowCategories.setter
    def ShowCategories(self, value: bool) -> None: ...
    @ShowDescription.setter
    def ShowDescription(self, value: bool) -> None: ...


class ThemedSegmentedButtonHandler:
    def __init__(self): ...
    def AttachEvent(self, id: str) -> None: ...
    def ClearItems(self) -> None: ...
    def ClearSelection(self) -> None: ...
    @property
    def SelectedIndex(self) -> int: ...
    @property
    def SelectedIndexes(self) -> Iterable[int]: ...
    @property
    def SelectionMode(self) -> SegmentedSelectionMode: ...
    @property
    def Spacing(self) -> int: ...
    def InsertItem(self, index: int, item: SegmentedItem) -> None: ...
    def OnLoad(self, e: EventArgs) -> None: ...
    def OnPreLoad(self, e: EventArgs) -> None: ...
    def RemoveItem(self, index: int, item: SegmentedItem) -> None: ...
    def SelectAll(self) -> None: ...
    @SelectedIndex.setter
    def SelectedIndex(self, value: int) -> None: ...
    @SelectedIndexes.setter
    def SelectedIndexes(self, value: Iterable[int]) -> None: ...
    @SelectionMode.setter
    def SelectionMode(self, value: SegmentedSelectionMode) -> None: ...
    @Spacing.setter
    def Spacing(self, value: int) -> None: ...
    def SetItem(self, index: int, item: SegmentedItem) -> None: ...




class ThemedSpinnerDirection:
    Clockwise = 1
    CounterClockwise = -1


class ThemedSpinnerHandler:
    def __init__(self): ...
    @property
    def Direction(self) -> ThemedSpinnerDirection: ...
    @property
    def DisabledAlpha(self) -> Single: ...
    @property
    def ElementColor(self) -> Color: ...
    @property
    def ElementSize(self) -> Single: ...
    @property
    def Enabled(self) -> bool: ...
    @property
    def Increment(self) -> Single: ...
    @property
    def LineCap(self) -> PenLineCap: ...
    @property
    def LineThickness(self) -> Single: ...
    @property
    def Mode(self) -> ThemedSpinnerMode: ...
    @property
    def NumberOfElements(self) -> int: ...
    @property
    def NumberOfVisibleElements(self) -> int: ...
    @property
    def Speed(self) -> float: ...
    def OnLoadComplete(self, e: EventArgs) -> None: ...
    def OnUnLoad(self, e: EventArgs) -> None: ...
    @Direction.setter
    def Direction(self, value: ThemedSpinnerDirection) -> None: ...
    @DisabledAlpha.setter
    def DisabledAlpha(self, value: Single) -> None: ...
    @ElementColor.setter
    def ElementColor(self, value: Color) -> None: ...
    @ElementSize.setter
    def ElementSize(self, value: Single) -> None: ...
    @Enabled.setter
    def Enabled(self, value: bool) -> None: ...
    @Increment.setter
    def Increment(self, value: Single) -> None: ...
    @LineCap.setter
    def LineCap(self, value: PenLineCap) -> None: ...
    @LineThickness.setter
    def LineThickness(self, value: Single) -> None: ...
    @Mode.setter
    def Mode(self, value: ThemedSpinnerMode) -> None: ...
    @NumberOfElements.setter
    def NumberOfElements(self, value: int) -> None: ...
    @NumberOfVisibleElements.setter
    def NumberOfVisibleElements(self, value: int) -> None: ...
    @Speed.setter
    def Speed(self, value: float) -> None: ...


class ThemedSpinnerMode:
    Line = 0
    Circle = 1


class ThemedSplitterHandler:
    def __init__(self): ...
    @property
    def FixedPanel(self) -> SplitterFixedPanel: ...
    @property
    def Orientation(self) -> Orientation: ...
    @property
    def Panel1(self) -> Control: ...
    @property
    def Panel1MinimumSize(self) -> int: ...
    @property
    def Panel2(self) -> Control: ...
    @property
    def Panel2MinimumSize(self) -> int: ...
    @property
    def Position(self) -> int: ...
    @property
    def RelativePosition(self) -> float: ...
    @property
    def Splitter(self) -> Panel: ...
    @property
    def SplitterWidth(self) -> int: ...
    @FixedPanel.setter
    def FixedPanel(self, value: SplitterFixedPanel) -> None: ...
    @Orientation.setter
    def Orientation(self, value: Orientation) -> None: ...
    @Panel1.setter
    def Panel1(self, value: Control) -> None: ...
    @Panel1MinimumSize.setter
    def Panel1MinimumSize(self, value: int) -> None: ...
    @Panel2.setter
    def Panel2(self, value: Control) -> None: ...
    @Panel2MinimumSize.setter
    def Panel2MinimumSize(self, value: int) -> None: ...
    @Position.setter
    def Position(self, value: int) -> None: ...
    @RelativePosition.setter
    def RelativePosition(self, value: float) -> None: ...
    @SplitterWidth.setter
    def SplitterWidth(self, value: int) -> None: ...


class ThemedStepperHandler:
    def __init__(self): ...
    def AttachEvent(self, id: str) -> None: ...
    @property
    def DownText(self) -> str: ...
    @property
    def Enabled(self) -> bool: ...
    @property
    def Font(self) -> Font: ...
    @property
    def Orientation(self) -> Orientation: ...
    @property
    def UpText(self) -> str: ...
    @property
    def ValidDirection(self) -> StepperValidDirections: ...
    @DownText.setter
    def DownText(self, value: str) -> None: ...
    @Enabled.setter
    def Enabled(self, value: bool) -> None: ...
    @Font.setter
    def Font(self, value: Font) -> None: ...
    @Orientation.setter
    def Orientation(self, value: Orientation) -> None: ...
    @UpText.setter
    def UpText(self, value: str) -> None: ...
    @ValidDirection.setter
    def ValidDirection(self, value: StepperValidDirections) -> None: ...


class ThemedTextStepperHandler:
    def __init__(self): ...
    def AttachEvent(self, id: str) -> None: ...
    @property
    def AutoSelectMode(self) -> AutoSelectMode: ...
    @property
    def BackgroundColor(self) -> Color: ...
    @property
    def CaretIndex(self) -> int: ...
    @property
    def Font(self) -> Font: ...
    @property
    def MaxLength(self) -> int: ...
    @property
    def PlaceholderText(self) -> str: ...
    @property
    def ReadOnly(self) -> bool: ...
    @property
    def Selection(self) -> Range: ...
    @property
    def ShowBorder(self) -> bool: ...
    @property
    def ShowStepper(self) -> bool: ...
    @property
    def Text(self) -> str: ...
    @property
    def TextAlignment(self) -> TextAlignment: ...
    @property
    def TextColor(self) -> Color: ...
    @property
    def ValidDirection(self) -> StepperValidDirections: ...
    def SelectAll(self) -> None: ...
    @AutoSelectMode.setter
    def AutoSelectMode(self, value: AutoSelectMode) -> None: ...
    @BackgroundColor.setter
    def BackgroundColor(self, value: Color) -> None: ...
    @CaretIndex.setter
    def CaretIndex(self, value: int) -> None: ...
    @Font.setter
    def Font(self, value: Font) -> None: ...
    @MaxLength.setter
    def MaxLength(self, value: int) -> None: ...
    @PlaceholderText.setter
    def PlaceholderText(self, value: str) -> None: ...
    @ReadOnly.setter
    def ReadOnly(self, value: bool) -> None: ...
    @Selection.setter
    def Selection(self, value: Range) -> None: ...
    @ShowBorder.setter
    def ShowBorder(self, value: bool) -> None: ...
    @ShowStepper.setter
    def ShowStepper(self, value: bool) -> None: ...
    @Text.setter
    def Text(self, value: str) -> None: ...
    @TextAlignment.setter
    def TextAlignment(self, value: TextAlignment) -> None: ...
    @TextColor.setter
    def TextColor(self, value: Color) -> None: ...
    @ValidDirection.setter
    def ValidDirection(self, value: StepperValidDirections) -> None: ...