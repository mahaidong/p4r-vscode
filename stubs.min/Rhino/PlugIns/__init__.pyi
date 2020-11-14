from typing import Tuple, Set, Iterable, List


class CustomRenderSaveFileTypes:
    def RegisterFileType(self, extensions: Iterable[str], description: str, saveFileHandler: SaveFileHandler) -> None: ...


class DescriptionType:
    Organization = 0
    Address = 1
    Country = 2
    Phone = 3
    WebSite = 4
    Email = 5
    UpdateUrl = 6
    Fax = 7
    Icon = 8


class DigitizerPlugIn(PlugIn):
    def SendPoint(self, point: Point3d, mousebuttons: MouseButton, shiftKey: bool, controlKey: bool) -> None: ...
    def SendRay(self, ray: Ray3d, mousebuttons: MouseButton, shiftKey: bool, controlKey: bool) -> None: ...


class FileExportPlugIn(PlugIn):


class FileImportPlugIn(PlugIn):


class FileTypeList:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, description: str, extension: str): ...
    @overload
    def __init__(self, description: str, extension: str, showOptionsButtonInFileDialog: bool): ...
    @overload
    def AddFileType(self, description: str, extension: str) -> int: ...
    @overload
    def AddFileType(self, description: str, extensions: Iterable[str]) -> int: ...
    @overload
    def AddFileType(self, description: str, extension: str, showOptionsButtonInFileDialog: bool) -> int: ...
    @overload
    def AddFileType(self, description: str, extension1: str, extension2: str) -> int: ...
    @overload
    def AddFileType(self, description: str, extensions: Iterable[str], showOptionsButtonInFileDialog: bool) -> int: ...
    @overload
    def AddFileType(self, description: str, extension1: str, extension2: str, showOptionsButtonInFileDialog: bool) -> int: ...


class LicenseBuildType:
    Unspecified = 0
    Release = 100
    Evaluation = 200
    Beta = 300


class LicenseCapabilities:
    NoCapabilities = 0
    CanBePurchased = 1
    CanBeSpecified = 2
    CanBeEvaluated = 4
    EvaluationIsExpired = 8
    SupportsRhinoAccounts = 16
    SupportsStandalone = 32
    SupportsZooPerUser = 64
    SupportsZooPerCore = 128


class LicenseChangedEventArgs:
    def __init__(self): ...


class LicenseData:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, productLicense: str, serialNumber: str, licenseTitle: str): ...
    @overload
    def __init__(self, productLicense: str, serialNumber: str, licenseTitle: str, buildType: LicenseBuildType): ...
    @overload
    def __init__(self, productLicense: str, serialNumber: str, licenseTitle: str, buildType: LicenseBuildType, licenseCount: int): ...
    @overload
    def __init__(self, productLicense: str, serialNumber: str, licenseTitle: str, buildType: LicenseBuildType, licenseCount: int, expirationDate: Nullable): ...
    @overload
    def __init__(self, productLicense: str, serialNumber: str, licenseTitle: str, buildType: LicenseBuildType, licenseCount: int, expirationDate: Nullable, productIcon: Icon): ...
    @overload
    def __init__(self, productLicense: str, serialNumber: str, licenseTitle: str, buildType: LicenseBuildType, licenseCount: int, expirationDate: Nullable, productIcon: Icon, requiresOnlineValidation: bool, isUpgradeFromPreviousVersion: bool): ...
    def Dispose(self) -> None: ...
    @property
    def BuildType(self) -> LicenseBuildType: ...
    @property
    def DateToExpire(self) -> Nullable: ...
    @property
    def ErrorMessage(self) -> str: ...
    @property
    def IsUpgradeFromPreviousVersion(self) -> bool: ...
    @property
    def LicenseCount(self) -> int: ...
    @property
    def LicenseExpires(self) -> bool: ...
    @property
    def LicenseTitle(self) -> str: ...
    @property
    def ProductIcon(self) -> Icon: ...
    @property
    def ProductLicense(self) -> str: ...
    @property
    def RequiresOnlineValidation(self) -> bool: ...
    @property
    def SerialNumber(self) -> str: ...
    def IsNotValid(data: LicenseData) -> bool: ...
    @overload
    def IsValid(self) -> bool: ...
    @overload
    def IsValid(data: LicenseData) -> bool: ...
    @overload
    def IsValid(self, ignoreExpirationDate: bool) -> bool: ...
    @BuildType.setter
    def BuildType(self, value: LicenseBuildType) -> None: ...
    @DateToExpire.setter
    def DateToExpire(self, value: Nullable) -> None: ...
    @ErrorMessage.setter
    def ErrorMessage(self, value: str) -> None: ...
    @IsUpgradeFromPreviousVersion.setter
    def IsUpgradeFromPreviousVersion(self, value: bool) -> None: ...
    @LicenseCount.setter
    def LicenseCount(self, value: int) -> None: ...
    @LicenseTitle.setter
    def LicenseTitle(self, value: str) -> None: ...
    @ProductIcon.setter
    def ProductIcon(self, value: Icon) -> None: ...
    @ProductLicense.setter
    def ProductLicense(self, value: str) -> None: ...
    @RequiresOnlineValidation.setter
    def RequiresOnlineValidation(self, value: bool) -> None: ...
    @SerialNumber.setter
    def SerialNumber(self, value: str) -> None: ...


class LicenseIdAttribute:
    def __init__(self, value: str): ...
    @property
    def Value(self) -> str: ...


class LicenseLease:
    @overload
    def __init__(self, unmanagedPointer: IntPtr): ...
    @overload
    def __init__(self, productId: str, groupName: str, groupId: str, userName: str, userId: str, productTitle: str, productVersion: str, productEdition: str, leaseId: str, iat: DateTime, exp: DateTime): ...
    @overload
    def __init__(self, productId: str, groupName: str, groupId: str, userName: str, userId: str, productTitle: str, productVersion: str, productEdition: str, leaseId: str, iat: DateTime, exp: DateTime, renewable_until: DateTime): ...
    @property
    def Expiration(self) -> DateTime: ...
    @property
    def GroupId(self) -> str: ...
    @property
    def GroupName(self) -> str: ...
    @property
    def IssuedAt(self) -> DateTime: ...
    @property
    def LeaseId(self) -> str: ...
    @property
    def ProductEdition(self) -> str: ...
    @property
    def ProductId(self) -> str: ...
    @property
    def ProductTitle(self) -> str: ...
    @property
    def ProductVersion(self) -> str: ...
    @property
    def UserId(self) -> str: ...
    @property
    def UserName(self) -> str: ...


class LicenseLeaseChangedEventArgs:
    def __init__(self, lease: LicenseLease): ...
    @property
    def Lease(self) -> LicenseLease: ...


class LicenseStatus:
    def __init__(self): ...
    @property
    def BuildType(self) -> LicenseBuildType: ...
    @property
    def CheckOutExpirationDate(self) -> Nullable: ...
    @property
    def CloudZooLeaseExpiration(self) -> Nullable: ...
    @property
    def CloudZooLeaseIsValid(self) -> bool: ...
    @property
    def ExpirationDate(self) -> Nullable: ...
    @property
    def LicenseTitle(self) -> str: ...
    @property
    def LicenseType(self) -> LicenseType: ...
    @property
    def PluginId(self) -> Guid: ...
    @property
    def ProductIcon(self) -> Icon: ...
    @property
    def ProductId(self) -> Guid: ...
    @property
    def RegisteredOrganization(self) -> str: ...
    @property
    def RegisteredOwner(self) -> str: ...
    @property
    def SerialNumber(self) -> str: ...
    @BuildType.setter
    def BuildType(self, value: LicenseBuildType) -> None: ...
    @CheckOutExpirationDate.setter
    def CheckOutExpirationDate(self, value: Nullable) -> None: ...
    @CloudZooLeaseExpiration.setter
    def CloudZooLeaseExpiration(self, value: Nullable) -> None: ...
    @CloudZooLeaseIsValid.setter
    def CloudZooLeaseIsValid(self, value: bool) -> None: ...
    @ExpirationDate.setter
    def ExpirationDate(self, value: Nullable) -> None: ...
    @LicenseTitle.setter
    def LicenseTitle(self, value: str) -> None: ...
    @LicenseType.setter
    def LicenseType(self, value: LicenseType) -> None: ...
    @PluginId.setter
    def PluginId(self, value: Guid) -> None: ...
    @ProductIcon.setter
    def ProductIcon(self, value: Icon) -> None: ...
    @ProductId.setter
    def ProductId(self, value: Guid) -> None: ...
    @RegisteredOrganization.setter
    def RegisteredOrganization(self, value: str) -> None: ...
    @RegisteredOwner.setter
    def RegisteredOwner(self, value: str) -> None: ...
    @SerialNumber.setter
    def SerialNumber(self, value: str) -> None: ...


class LicenseType:
    Standalone = 0
    Network = 1
    NetworkLoanedOut = 2
    NetworkCheckedOut = 3
    CloudZoo = 4


class LicenseUtils:
    @overload
    def AskUserForLicense(productType: int, standAlone: bool, parentWindow: Object, textMask: str, validateProductKeyDelegate: ValidateProductKeyDelegate, onLeaseChangedDelegate: OnLeaseChangedDelegate, product_path: str, product_title: str, pluginId: Guid, licenseId: Guid, capabilities: LicenseCapabilities) -> bool: ...
    @overload
    def AskUserForLicense(productType: int, standAlone: bool, parentWindow: Object, textMask: str, validateProductKeyDelegate: ValidateProductKeyDelegate, onLeaseChangedDelegate: OnLeaseChangedDelegate, verifyLicenseKeyDelegate: VerifyLicenseKeyDelegate, verifyPreviousVersionLicenseKeyDelegate: VerifyPreviousVersionLicenseDelegate, product_path: str, product_title: str, pluginId: Guid, licenseId: Guid, capabilities: LicenseCapabilities) -> bool: ...
    def CheckInLicense(productId: Guid) -> bool: ...
    def CheckOutLicense(productId: Guid) -> bool: ...
    def ConvertLicense(productId: Guid) -> bool: ...
    def DeleteLicense(productId: Guid) -> bool: ...
    def Echo(message: str) -> str: ...
    @overload
    def GetLicense(validateProductKeyDelegate: ValidateProductKeyDelegate, leaseChangedDelegate: OnLeaseChangedDelegate, product_type: int, capabilities: int, textMask: str, product_path: str, product_title: str, pluginId: Guid, licenseId: Guid) -> bool: ...
    @overload
    def GetLicense(validateProductKeyDelegate: ValidateProductKeyDelegate, leaseChangedDelegate: OnLeaseChangedDelegate, verifyLicenseKeyDelegate: VerifyLicenseKeyDelegate, verifyPreviousVersionLicenseKeyDelegate: VerifyPreviousVersionLicenseDelegate, product_type: int, capabilities: int, textMask: str, product_path: str, product_title: str, pluginId: Guid, licenseId: Guid) -> bool: ...
    def GetLicenseCapabilities(filter: int) -> LicenseCapabilities: ...
    def GetLicenseStatus() -> Set(LicenseStatus): ...
    def GetLicenseType(productId: Guid) -> int: ...
    def GetOneLicenseStatus(productid: Guid) -> LicenseStatus: ...
    def Initialize() -> bool: ...
    def IsCheckOutEnabled() -> bool: ...
    def LicenseOptionsHandler(pluginId: Guid, licenseId: Guid, productTitle: str, standAlone: bool) -> bool: ...
    def LoginToCloudZoo() -> bool: ...
    def LogoutOfCloudZoo() -> bool: ...
    def ReturnLicense(productId: Guid) -> bool: ...
    def ShowBuyLicenseUi(productId: Guid) -> None: ...
    def ShowLicenseValidationUi(cdkey: str) -> bool: ...
    def ShowRhinoExpiredMessage(mode: Mode, result: int) -> Tuple[bool, int]: ...


class LoadPlugInResult:
    Success = 0
    SuccessAlreadyLoaded = 1
    ErrorUnknown = 2


class LoadReturnCode:
    ErrorShowDialog = 0
    Success = 1
    ErrorNoDialog = -1


class OnLeaseChangedDelegate:
    def __init__(self, object: Object, method: IntPtr): ...
    def BeginInvoke(self, args: LicenseLeaseChangedEventArgs, callback: AsyncCallback, object: Object) -> Tuple[IAsyncResult, Icon]: ...
    def EndInvoke(self, result: IAsyncResult) -> Tuple[Icon]: ...
    def Invoke(self, args: LicenseLeaseChangedEventArgs) -> Tuple[Icon]: ...


class PlugIn:
    def add_SettingsSaved(self, value: EventHandler) -> None: ...
    def CommandSettings(self, name: str) -> PersistentSettings: ...
    @overload
    def Find(pluginAssembly: Assembly) -> PlugIn: ...
    @overload
    def Find(plugInId: Guid) -> PlugIn: ...
    def FlushSettingsSavedQueue() -> None: ...
    @property
    def AskOnLoadProtection() -> bool: ...
    @property
    def Assembly(self) -> Assembly: ...
    @property
    def Description(self) -> str: ...
    @property
    def Id(self) -> Guid: ...
    @property
    def InstalledPlugInCount() -> int: ...
    @property
    def LicenseId(self) -> Guid: ...
    @property
    def LoadAtStartup(self) -> bool: ...
    @property
    def LoadTime(self) -> PlugInLoadTime: ...
    @property
    def Name(self) -> str: ...
    @property
    def Settings(self) -> PersistentSettings: ...
    @property
    def SettingsDirectory(self) -> str: ...
    @property
    def SettingsDirectoryAllUsers(self) -> str: ...
    @property
    def Version(self) -> str: ...
    @property
    def WindowPositionSettings(self) -> PersistentSettings: ...
    def GetCommands(self) -> Set(Command): ...
    def GetEnglishCommandNames(pluginId: Guid) -> Set(str): ...
    def GetInstalledPlugInFolders() -> Set(str): ...
    @overload
    def GetInstalledPlugInNames() -> Set(str): ...
    @overload
    def GetInstalledPlugInNames(typeFilter: PlugInType, loaded: bool, unloaded: bool) -> Set(str): ...
    def GetInstalledPlugIns() -> Dictionary: ...
    def GetLoadProtection(pluginId: Guid) -> Tuple[bool, bool]: ...
    def GetPlugInInfo(pluginId: Guid) -> PlugInInfo: ...
    def GetPlugInObject(self) -> Object: ...
    def GetPluginSettings(plugInId: Guid, load: bool) -> PersistentSettings: ...
    def Icon(self, size: Size) -> Bitmap: ...
    def IdFromName(pluginName: str) -> Guid: ...
    def IdFromPath(pluginPath: str) -> Guid: ...
    def LoadComputeExtensionPlugins() -> None: ...
    @overload
    def LoadPlugIn(pluginId: Guid) -> bool: ...
    @overload
    def LoadPlugIn(path: str) -> Tuple[LoadPlugInResult, Guid]: ...
    @overload
    def LoadPlugIn(pluginId: Guid, loadQuietly: bool, forceLoad: bool) -> bool: ...
    def NameFromPath(pluginPath: str) -> str: ...
    def PathFromId(pluginId: Guid) -> str: ...
    def PathFromName(pluginName: str) -> str: ...
    def PlugInExists(id: Guid) -> Tuple[bool, bool, bool]: ...
    def RaiseOnPlugInSettingsSavedEvent() -> None: ...
    def remove_SettingsSaved(self, value: EventHandler) -> None: ...
    def SavePluginSettings(plugInId: Guid) -> None: ...
    def SaveSettings(self) -> None: ...
    @AskOnLoadProtection.setter
    def AskOnLoadProtection(value: bool) -> None: ...
    def SetLoadProtection(pluginId: Guid, loadSilently: bool) -> None: ...


class PlugInDescriptionAttribute:
    def __init__(self, descriptionType: DescriptionType, value: str): ...
    @property
    def DescriptionType(self) -> DescriptionType: ...
    @property
    def Value(self) -> str: ...


class PlugInInfo:
    @property
    def Address(self) -> str: ...
    @property
    def CommandNames(self) -> Set(str): ...
    @property
    def Country(self) -> str: ...
    @property
    def Description(self) -> str: ...
    @property
    def Email(self) -> str: ...
    @property
    def Fax(self) -> str: ...
    @property
    def FileName(self) -> str: ...
    @property
    def FileTypeDescriptions(self) -> Set(str): ...
    @property
    def FileTypeExtensions(self) -> Set(str): ...
    @property
    def Id(self) -> Guid: ...
    @property
    def IsDotNet(self) -> bool: ...
    @property
    def IsLoaded(self) -> bool: ...
    @property
    def Name(self) -> str: ...
    @property
    def Organization(self) -> str: ...
    @property
    def Phone(self) -> str: ...
    @property
    def PlugInLoadTime(self) -> PlugInLoadTime: ...
    @property
    def PlugInType(self) -> PlugInType: ...
    @property
    def RegistryPath(self) -> str: ...
    @property
    def ShipsWithRhino(self) -> bool: ...
    @property
    def UpdateUrl(self) -> str: ...
    @property
    def Version(self) -> str: ...
    @property
    def WebSite(self) -> str: ...
    def Icon(self, size: Size) -> Bitmap: ...
    def IsLoadProtected(self) -> Tuple[bool, bool]: ...


class PlugInLoadTime:
    Disabled = 0
    AtStartup = 1
    WhenNeeded = 2
    WhenNeededIgnoreDockingBars = 6
    WhenNeededOrOptionsDialog = 10
    WhenNeededOrTabbedDockBar = 18


class PlugInType:
    #None = 0
    Render = 1
    FileImport = 2
    FileExport = 4
    Digitizer = 8
    Utility = 16
    DisplayPipeline = 32
    DisplayEngine = 64
    Any = 127


class PreviewNotification:
    def NotifyIntermediateUpdate(self, rw: RenderWindow) -> None: ...


class PreviewRenderTypes:
    #None = 0
    ThreeSeparateImages = 1
    SingleImage = 2
    Progressive = 3


class RenderFeature:
    Materials = 0
    Environments = 1
    Textures = 2
    PostEffects = 3
    Sun = 4
    CustomRenderMeshes = 5
    Decals = 6
    GroundPlane = 7
    SkyLight = 8
    CustomDecalProperties = 9
    LinearWorkflow = 10
    Exposure = 11
    ShadowOnlyGroundPlane = 12
    RenderBlowup = 13
    RenderWindow = 14
    RenderInWindow = 15
    FocalBlur = 17
    RenderArctic = 18
    RenderViewSource = 19
    CustomSkylightEnvironment = 20
    CustomReflectionEnvironment = 21


class RenderPlugIn(PlugIn):
    def CurrentRendererSupportsFeature(feature: RenderFeature) -> bool: ...
    def EnableAssignMaterialButton(self) -> bool: ...
    def EnableCreateMaterialButton(self) -> bool: ...
    def EnableEditMaterialButton(self, doc: RhinoDoc, material: Material) -> bool: ...
    @property
    def PerferBasicContent(self) -> bool: ...
    def GetRenderSettingsSections(self) -> List: ...
    def OnAssignMaterial(self, parent: IntPtr, doc: RhinoDoc, material: Material) -> Tuple[bool, Material]: ...
    def OnCreateMaterial(self, parent: IntPtr, doc: RhinoDoc, material: Material) -> Tuple[bool, Material]: ...
    def OnEditMaterial(self, parent: IntPtr, doc: RhinoDoc, material: Material) -> Tuple[bool, Material]: ...
    def RenderSettingsCustomSections(self, sections: List) -> None: ...
    @PerferBasicContent.setter
    def PerferBasicContent(self, value: bool) -> None: ...
    def SunCustomSections(self, sections: List) -> None: ...


class SaveFileHandler:
    def __init__(self, object: Object, method: IntPtr): ...
    def BeginInvoke(self, fileName: str, includeAlpha: bool, renderWindow: RenderWindow, callback: AsyncCallback, object: Object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> bool: ...
    def Invoke(self, fileName: str, includeAlpha: bool, renderWindow: RenderWindow) -> bool: ...


class ValidateProductKeyDelegate:
    def __init__(self, object: Object, method: IntPtr): ...
    def BeginInvoke(self, productKey: str, callback: AsyncCallback, object: Object) -> Tuple[IAsyncResult, LicenseData]: ...
    def EndInvoke(self, result: IAsyncResult) -> Tuple[ValidateResult, LicenseData]: ...
    def Invoke(self, productKey: str) -> Tuple[ValidateResult, LicenseData]: ...


class ValidateResult:
    ErrorShowMessage = 0
    Success = 1
    ErrorHideMessage = -1


class VerifyLicenseKeyDelegate:
    def __init__(self, object: Object, method: IntPtr): ...
    def BeginInvoke(self, licenseKey: str, validationCode: str, validationCodeInstallDate: DateTime, gracePeriodExpired: bool, callback: AsyncCallback, object: Object) -> Tuple[IAsyncResult, LicenseData]: ...
    def EndInvoke(self, result: IAsyncResult) -> Tuple[ValidateResult, LicenseData]: ...
    def Invoke(self, licenseKey: str, validationCode: str, validationCodeInstallDate: DateTime, gracePeriodExpired: bool) -> Tuple[ValidateResult, LicenseData]: ...


class VerifyPreviousVersionLicenseDelegate:
    def __init__(self, object: Object, method: IntPtr): ...
    def BeginInvoke(self, license: str, previousVersionLicense: str, callback: AsyncCallback, object: Object) -> Tuple[IAsyncResult, str]: ...
    def EndInvoke(self, result: IAsyncResult) -> Tuple[bool, str]: ...
    def Invoke(self, license: str, previousVersionLicense: str) -> Tuple[bool, str]: ...


class WriteFileResult:
    Failure = 0
    Success = 1
    Cancel = -1
