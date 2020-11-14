from typing import Tuple, Set, Iterable, List


class BakingFunctions:
    #None = 0
    Decals = 1
    ProceduralTextures = 2
    CustomObjectMappings = 4
    WcsBasedMappings = 8
    MultipleMappingChannels = 16
    NoRepeatTextures = 32
    All = 4294967295


class ChangeQueue:
    def AreViewsEqual(self, aView: ViewInfo, bView: ViewInfo) -> bool: ...
    def ConvertCameraBasedLightToWorld(changequeue: ChangeQueue, light: Light, vp: ViewInfo) -> None: ...
    def CrcFromGuid(guid: Guid) -> UInt32: ...
    @overload
    def CreateWorld(self) -> None: ...
    @overload
    def CreateWorld(self, bFlushWhenReady: bool) -> None: ...
    def Dispose(self) -> None: ...
    def EnvironmentForid(self, crc: UInt32) -> RenderEnvironment: ...
    def EnvironmentIdForUsage(self, usage: Usage) -> UInt32: ...
    def Flush(self) -> None: ...
    @property
    def DisplayPipelineAttributes(self) -> DisplayPipelineAttributes: ...
    @property
    def IsPreview(self) -> bool: ...
    @property
    def ViewId(self) -> Guid: ...
    def GetQueueGroundPlane(self) -> GroundPlane: ...
    def GetQueueRenderSettings(self) -> RenderSettings: ...
    def GetQueueSceneBoundingBox(self) -> BoundingBox: ...
    def GetQueueSkylight(self) -> Skylight: ...
    def GetQueueSun(self) -> Light: ...
    def GetQueueView(self) -> ViewInfo: ...
    def MaterialFromId(self, crc: UInt32) -> RenderMaterial: ...
    def OneShot(self) -> None: ...


class ClippingPlane:
    @property
    def Attributes(self) -> ObjectAttributes: ...
    @property
    def Id(self) -> Guid: ...
    @property
    def IsEnabled(self) -> bool: ...
    @property
    def Plane(self) -> Plane: ...
    @property
    def ViewIds(self) -> List: ...


class DisplayRenderSettings:
    @property
    def CullBackFaces(self) -> bool: ...
    @property
    def ForceFlatShading(self) -> bool: ...
    @property
    def SceneLightingOn(self) -> bool: ...


class DynamicObjectTransform:
    @property
    def MeshInstanceId(self) -> UInt32: ...
    @property
    def Transform(self) -> Transform: ...
    def ToString(self) -> str: ...


class Environment:


class Event:
    Added = 0
    Deleted = 1
    Undeleted = 2
    Modified = 3
    Sorted = 4


class FrameBufferFillMode:
    #None = 0
    DefaultColor = 1
    SolidColor = 2
    Gradient2Color = 3
    Gradient4Color = 4
    Bitmap = 5
    Renderer = 6
    Transparent = 7
    Force32Bit = 4294967295


class GroundPlane:
    @property
    def Altitude(self) -> float: ...
    @property
    def Crc(self) -> UInt32: ...
    @property
    def Enabled(self) -> bool: ...
    @property
    def IsShadowOnly(self) -> bool: ...
    @property
    def MaterialId(self) -> UInt32: ...
    @property
    def TextureOffset(self) -> Vector2d: ...
    @property
    def TextureRotation(self) -> float: ...
    @property
    def TextureScale(self) -> Vector2d: ...


class Light:
    @property
    def ChangeType(self) -> Event: ...
    @property
    def Data(self) -> Light: ...
    @property
    def Id(self) -> Guid: ...
    @property
    def IdCrc(self) -> UInt32: ...


class MappingChannel:
    @property
    def Local(self) -> Transform: ...
    @property
    def Mapping(self) -> TextureMapping: ...


class MappingChannelCollection:
    @property
    def Channels(self) -> Iterable[MappingChannel]: ...
    @property
    def Count(self) -> int: ...
    @property
    def Item(self, i: int) -> MappingChannel: ...


class Material:
    @property
    def Id(self) -> UInt32: ...
    @property
    def MeshIndex(self) -> int: ...
    @property
    def MeshInstanceId(self) -> UInt32: ...


class Mesh:
    @property
    def Attributes(self) -> ObjectAttributes: ...
    @property
    def Mapping(self) -> MappingChannelCollection: ...
    @property
    def Object(self) -> RhinoObject: ...
    @property
    def SingleMapping(self) -> MappingChannel: ...
    def GetMeshes(self) -> Set(Mesh): ...
    def Id(self) -> Guid: ...


class MeshInstance:
    @property
    def CastShadows(self) -> bool: ...
    @property
    def GroupId(self) -> UInt32: ...
    @property
    def InstanceId(self) -> UInt32: ...
    @property
    def MaterialId(self) -> UInt32: ...
    @property
    def MeshId(self) -> Guid: ...
    @property
    def MeshIndex(self) -> int: ...
    @property
    def ReceiveShadows(self) -> bool: ...
    @property
    def RenderMaterial(self) -> RenderMaterial: ...
    @property
    def Transform(self) -> Transform: ...


class Skylight:
    @property
    def Enabled(self) -> bool: ...
    @property
    def ShadowIntensity(self) -> float: ...
    @property
    def UsesCustomEnvironment(self) -> bool: ...
    def ToString(self) -> str: ...