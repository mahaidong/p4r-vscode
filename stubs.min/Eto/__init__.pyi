__all__ = ['Drawing','Forms','IO','Threading']
from typing import Tuple, Set, Iterable, List


class AttachableMemberIdentifier:
    def __init__(self, declaringType: Type, memberName: str): ...
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    def Equals(self, other: AttachableMemberIdentifier) -> bool: ...
    @property
    def DeclaringType(self) -> Type: ...
    @property
    def MemberName(self) -> str: ...
    def GetHashCode(self) -> int: ...
    def op_Equality(left: AttachableMemberIdentifier, right: AttachableMemberIdentifier) -> bool: ...
    def op_Inequality(left: AttachableMemberIdentifier, right: AttachableMemberIdentifier) -> bool: ...
    def ToString(self) -> str: ...


class AutoInitializeAttribute:
    def __init__(self, initialize: bool): ...
    @property
    def Initialize(self) -> bool: ...




class ContentPropertyAttribute:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, name: str): ...
    @property
    def Name(self) -> str: ...




class DefaultStyleProvider:
    def __init__(self): ...
    def Add(self, style: str, handler: Action) -> None: ...
    def add_StyleWidget(self, value: Action) -> None: ...
    def Clear(self) -> None: ...
    @property
    def Inherit(self) -> bool: ...
    def remove_StyleWidget(self, value: Action) -> None: ...
    @Inherit.setter
    def Inherit(self, value: bool) -> None: ...






class EtoEnvironment:
    @property
    def Is64BitProcess() -> bool: ...
    @property
    def Platform() -> OperatingSystemPlatform: ...
    def GetFolderPath(folder: EtoSpecialFolder) -> str: ...


class EtoMemberIdentifier(AttachableMemberIdentifier):
    def __init__(self, declaringType: Type, memberName: str): ...


class EtoSpecialFolder:
    ApplicationSettings = 0
    ApplicationResources = 1
    Documents = 2


class ExportHandlerAttribute(PlatformExtensionAttribute):
    def __init__(self, widgetType: Type, handlerType: Type): ...
    @property
    def HandlerType(self) -> Type: ...
    @property
    def WidgetType(self) -> Type: ...
    def Register(self, platform: Platform) -> None: ...


class ExportInitializerAttribute(PlatformExtensionAttribute):
    def __init__(self, initializerType: Type): ...
    @property
    def InitializerType(self) -> Type: ...
    def Register(self, platform: Platform) -> None: ...




class FileAction:
    OpenFile = 0
    SaveFile = 1
    SelectFolder = 2


class HandlerAttribute:
    def __init__(self, type: Type): ...
    @property
    def Type(self) -> Type: ...


class HandlerCreatedEventArgs:
    def __init__(self, instance: Object): ...
    @property
    def Instance(self) -> Object: ...


class ICallback:


class ICallbackSource:
    @property
    def Callback(self) -> Object: ...


class IControlObjectSource:
    @property
    def ControlObject(self) -> Object: ...


class IHandler:
    @property
    def ID(self) -> str: ...
    @property
    def NativeHandle(self) -> IntPtr: ...
    @property
    def Widget(self) -> Widget: ...
    def HandleEvent(self, id: str, defaultEvent: bool) -> None: ...
    def Initialize(self) -> None: ...
    @ID.setter
    def ID(self, value: str) -> None: ...
    @Widget.setter
    def Widget(self, value: Widget) -> None: ...


class IHandler:
    def GetFolderPath(self, folder: EtoSpecialFolder) -> str: ...


class IHandlerSource:
    @property
    def Handler(self) -> Object: ...


class IPlatformInitializer:
    def Initialize(self, platform: Platform) -> None: ...


class IStyleProvider:
    def ApplyCascadingStyle(self, container: Object, widget: Object, style: str) -> None: ...
    def ApplyDefault(self, widget: Object) -> None: ...
    def ApplyStyle(self, widget: Object, style: str) -> None: ...
    @property
    def Inherit(self) -> bool: ...


class NamespaceInfo:
    @overload
    def __init__(self, ns: str): ...
    @overload
    def __init__(self, ns: str, assembly: Assembly): ...
    @overload
    def FindResource(self) -> Stream: ...
    @overload
    def FindResource(self, resourceName: str) -> Stream: ...
    def FindType(self, typeName: str) -> Type: ...
    @property
    def Assembly(self) -> Assembly: ...
    @property
    def Namespace(self) -> str: ...
    @Assembly.setter
    def Assembly(self, value: Assembly) -> None: ...


class OperatingSystemPlatform:
    def __init__(self): ...
    @property
    def IsLinux(self) -> bool: ...
    @property
    def IsMac(self) -> bool: ...
    @property
    def IsMono(self) -> bool: ...
    @property
    def IsUnix(self) -> bool: ...
    @property
    def IsWindows(self) -> bool: ...
    @property
    def IsWinRT(self) -> bool: ...


class Platform:
    def add_HandlerCreated(self, value: EventHandler) -> None: ...
    @overload
    def Add(self, instantiator: Func) -> None: ...
    @overload
    def Add(self, type: Type, instantiator: Func) -> None: ...
    def add_WidgetCreated(self, value: EventHandler) -> None: ...
    def Cache(self, cacheKey: Object) -> Dictionary: ...
    @overload
    def Create(self) -> T: ...
    @overload
    def Create(self, type: Type) -> Object: ...
    @overload
    def CreateShared(self) -> T: ...
    @overload
    def CreateShared(self, type: Type) -> Object: ...
    @overload
    def Find(self) -> Func: ...
    @overload
    def Find(self, type: Type) -> Func: ...
    @property
    def AllowReinitialize() -> bool: ...
    @property
    def Context(self) -> IDisposable: ...
    @property
    def Detect() -> Platform: ...
    @property
    def ID(self) -> str: ...
    @property
    def Instance() -> Platform: ...
    @property
    def IsAndroid(self) -> bool: ...
    @property
    def IsDesktop(self) -> bool: ...
    @property
    def IsGtk(self) -> bool: ...
    @property
    def IsIos(self) -> bool: ...
    @property
    def IsMac(self) -> bool: ...
    @property
    def IsMobile(self) -> bool: ...
    @property
    def IsValid(self) -> bool: ...
    @property
    def IsWinForms(self) -> bool: ...
    @property
    def IsWpf(self) -> bool: ...
    def Get(generatorType: str) -> Platform: ...
    @property
    def SupportedFeatures(self) -> PlatformFeatures: ...
    @overload
    def Initialize(platformType: str) -> None: ...
    @overload
    def Initialize(platform: Platform) -> None: ...
    @overload
    def Invoke(self, action: Action) -> None: ...
    @overload
    def Invoke(self, action: Func) -> T: ...
    @overload
    def LoadAssembly(self, assembly: Assembly) -> None: ...
    @overload
    def LoadAssembly(self, assemblyName: str) -> None: ...
    def remove_HandlerCreated(self, value: EventHandler) -> None: ...
    def remove_WidgetCreated(self, value: EventHandler) -> None: ...
    @AllowReinitialize.setter
    def AllowReinitialize(value: bool) -> None: ...
    @overload
    def Supports(self) -> bool: ...
    @overload
    def Supports(self, type: Type) -> bool: ...
    def ThreadStart(self) -> IDisposable: ...


class PlatformExtensionAttribute:
    @property
    def PlatformID(self) -> str: ...
    def Register(self, platform: Platform) -> None: ...
    @PlatformID.setter
    def PlatformID(self, value: str) -> None: ...
    def Supports(self, platform: Platform) -> bool: ...


class PlatformFeatures:
    #None = 0
    CustomCellSupportsControlView = 1
    DrawableWithTransparentContent = 2
    TabIndexWithCustomContainers = 4


class Platforms:


class PropertyStore:
    def __init__(self, parent: Object): ...
    def AddEvent(self, key: Object, value: Delegate) -> None: ...
    def AddHandlerEvent(self, key: str, value: Delegate) -> None: ...
    @overload
    def Create(self, key: Object) -> T: ...
    @overload
    def Create(self, key: Object, create: Func) -> T: ...
    @property
    def Parent(self) -> Object: ...
    @overload
    def Get(self, key: Object, defaultValue: T) -> T: ...
    @overload
    def Get(self, key: Object, defaultValue: Func) -> T: ...
    def GetCommand(self, key: Object) -> ICommand: ...
    def RemoveEvent(self, key: Object, value: Delegate) -> None: ...
    @overload
    def Set(self, key: Object, value: T, defaultValue: T) -> None: ...
    @overload
    def Set(self, key: Object, value: T, propertyChanged: Action, defaultValue: T) -> bool: ...
    @overload
    def Set(self, key: Object, value: T, propertyChanged: PropertyChangedEventHandler, defaultValue: T, propertyName: str) -> bool: ...
    def SetCommand(self, key: Object, value: ICommand, setEnabled: Action, addExecute: Action, removeExecute: Action, getParameter: Func) -> None: ...
    def TriggerEvent(self, key: Object, sender: Object, args: T) -> None: ...
    def TrySet(self, key: Object, value: T, defaultValue: T) -> bool: ...
    def UpdateCommandCanExecute(self, key: Object) -> None: ...


class RuntimeNamePropertyAttribute:
    def __init__(self, name: str): ...
    @property
    def Name(self) -> str: ...


class Style:
    @overload
    def Add(style: str, handler: StyleWidgetHandler) -> None: ...
    @overload
    def Add(style: str, styleHandler: StyleHandler) -> None: ...
    def add_StyleWidget(value: Action) -> None: ...
    @property
    def Provider() -> IStyleProvider: ...
    def remove_StyleWidget(value: Action) -> None: ...
    @Provider.setter
    def Provider(value: IStyleProvider) -> None: ...






class UnhandledExceptionEventArgs:
    def __init__(self, exception: Object, isTerminating: bool): ...
    @property
    def ExceptionObject(self) -> Object: ...
    @property
    def IsTerminating(self) -> bool: ...


class Widget:
    def add_StyleChanged(self, value: EventHandler) -> None: ...
    def Dispose(self) -> None: ...
    @property
    def ControlObject(self) -> Object: ...
    @property
    def Handler(self) -> Object: ...
    @property
    def ID(self) -> str: ...
    @property
    def IsDisposed(self) -> bool: ...
    @property
    def NativeHandle(self) -> IntPtr: ...
    @property
    def Platform(self) -> Platform: ...
    @property
    def Properties(self) -> PropertyStore: ...
    @property
    def Style(self) -> str: ...
    def remove_StyleChanged(self, value: EventHandler) -> None: ...
    @ID.setter
    def ID(self, value: str) -> None: ...
    @Style.setter
    def Style(self, value: str) -> None: ...
    def ToString(self) -> str: ...


class WidgetCreatedEventArgs:
    def __init__(self, instance: Widget): ...
    @property
    def Instance(self) -> Widget: ...






