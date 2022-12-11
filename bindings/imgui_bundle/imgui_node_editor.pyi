"""Node editor built using ImGui
Python bindings for https://github.com/thedmd/imgui-node-editor
"""

from typing import Any, Optional
import numpy as np
import enum
from imgui_bundle.imgui import ImVec2, ImVec4, ImDrawList
from imgui_bundle import imgui


ImGuiMouseButton = imgui.MouseButton


EditorContext = Any


class NodeId:
    def __init__(self, id: int=0):
        pass
    def id(self) -> int:
        pass
    @staticmethod
    def create() -> NodeId:
        """Creates a new NodeId with a unique id

        Create your node once per session, not at each frame!
        """
        pass


class LinkId:
    def __init__(self, id: int=0):
        pass
    def id(self) -> int:
        pass
    @staticmethod
    def create() -> LinkId:
        """Creates a new LinkId with a unique id

        Create your node once per session, not at each frame!
        """
        pass


class PinId:
    def __init__(self, id: int=0):
        pass
    def id(self) -> int:
        pass
    @staticmethod
    def create() -> PinId:
        """Creates a new NodeId with a unique id

        Create your node once per session, not at each frame!
        """
        pass


# Suspends canvas by returning to normal ImGui transformation space.
# While suspended UI will not be drawn on canvas plane.
#
# Calls to Suspend()/Resume() are symmetrical. Each call to Suspend()
# must be matched with call to Resume().
def suspend_editor_canvas():
    pass
def resume_editor_canvas():
    pass

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# <litgen_stub> // Autogenerated code below! Do not edit!
####################    <generated_from:imgui_node_editor.h>    ####################
# ------------------------------------------------------------------------------
# VERSION 0.9.1
#
# LICENSE
#   This software is dual-licensed to the public domain and under the following
#   license: you are granted a perpetual, irrevocable license to copy, modify,
#   publish, and distribute this file as you see fit.
#
# CREDITS
#   Written by Michal Cichon
# ------------------------------------------------------------------------------
# # ifndef __IMGUI_NODE_EDITOR_H__
#

# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------

"""------------------------------------------------------------------------------"""
""" namespace Editor"""

# ------------------------------------------------------------------------------

class PinKind(enum.Enum):  # imgui_node_editor.h:41
    """------------------------------------------------------------------------------"""

    # Input,    /* original C++ signature */
    input = enum.auto()  # (= 0)
    # Output    /* original C++ signature */
    # }
    output = enum.auto()  # (= 1)

class FlowDirection(enum.Enum):  # imgui_node_editor.h:47
    # Forward,    /* original C++ signature */
    forward = enum.auto()  # (= 0)
    # Backward    /* original C++ signature */
    # }
    backward = enum.auto()  # (= 1)

class CanvasSizeMode(enum.Enum):  # imgui_node_editor.h:53
    # FitVerticalView,            /* original C++ signature */
    fit_vertical_view = (
        enum.auto()
    )  # (= 0)  # Previous view will be scaled to fit new view on Y axis
    # FitHorizontalView,          /* original C++ signature */
    fit_horizontal_view = (
        enum.auto()
    )  # (= 1)  # Previous view will be scaled to fit new view on X axis
    # CenterOnly,                 /* original C++ signature */
    center_only = enum.auto()  # (= 2)  # Previous view will be centered on new view

class SaveReasonFlags(enum.Enum):  # imgui_node_editor.h:62
    """------------------------------------------------------------------------------"""

    # None       = 0x00000000,    /* original C++ signature */
    none = enum.auto()  # (= 0x00000000)
    # Navigation = 0x00000001,    /* original C++ signature */
    navigation = enum.auto()  # (= 0x00000001)
    # Position   = 0x00000002,    /* original C++ signature */
    position = enum.auto()  # (= 0x00000002)
    # Size       = 0x00000004,    /* original C++ signature */
    size = enum.auto()  # (= 0x00000004)
    # Selection  = 0x00000008,    /* original C++ signature */
    selection = enum.auto()  # (= 0x00000008)
    # AddNode    = 0x00000010,    /* original C++ signature */
    add_node = enum.auto()  # (= 0x00000010)
    # RemoveNode = 0x00000020,    /* original C++ signature */
    remove_node = enum.auto()  # (= 0x00000020)
    # User       = 0x00000040    /* original C++ signature */
    # }
    user = enum.auto()  # (= 0x00000040)

class Config:  # imgui_node_editor.h:85

    # std::string             SettingsFile;    /* original C++ signature */
    settings_file: str  # imgui_node_editor.h:89
    # void*                   UserPointer;    /* original C++ signature */
    user_pointer: Any  # imgui_node_editor.h:96
    # CanvasSizeModeAlias     CanvasSizeMode;    /* original C++ signature */
    canvas_size_mode: CanvasSizeMode  # imgui_node_editor.h:98
    # int                     DragButtonIndex;    /* original C++ signature */
    drag_button_index: int  # Mouse button index drag action will react to (0-left, 1-right, 2-middle)    # imgui_node_editor.h:99
    # int                     SelectButtonIndex;    /* original C++ signature */
    select_button_index: int  # Mouse button index select action will react to (0-left, 1-right, 2-middle)    # imgui_node_editor.h:100
    # int                     NavigateButtonIndex;    /* original C++ signature */
    navigate_button_index: int  # Mouse button index navigate action will react to (0-left, 1-right, 2-middle)    # imgui_node_editor.h:101
    # int                     ContextMenuButtonIndex;    /* original C++ signature */
    context_menu_button_index: int  # Mouse button index context menu action will react to (0-left, 1-right, 2-middle)    # imgui_node_editor.h:102

    # Config()    /* original C++ signature */
    #         : SettingsFile("NodeEditor.json")
    #         , BeginSaveSession(nullptr)
    #         , EndSaveSession(nullptr)
    #         , SaveSettings(nullptr)
    #         , LoadSettings(nullptr)
    #         , SaveNodeSettings(nullptr)
    #         , LoadNodeSettings(nullptr)
    #         , UserPointer(nullptr)
    #         , CustomZoomLevels()
    #         , CanvasSizeMode(CanvasSizeModeAlias::FitVerticalView)
    #         , DragButtonIndex(0)
    #         , SelectButtonIndex(0)
    #         , NavigateButtonIndex(1)
    #         , ContextMenuButtonIndex(1)
    #     {
    #     }
    def __init__(self) -> None:  # imgui_node_editor.h:104
        pass

class StyleColor(enum.Enum):  # imgui_node_editor.h:125
    """------------------------------------------------------------------------------"""

    # StyleColor_Bg,    /* original C++ signature */
    bg = enum.auto()  # (= 0)
    # StyleColor_Grid,    /* original C++ signature */
    grid = enum.auto()  # (= 1)
    # StyleColor_NodeBg,    /* original C++ signature */
    node_bg = enum.auto()  # (= 2)
    # StyleColor_NodeBorder,    /* original C++ signature */
    node_border = enum.auto()  # (= 3)
    # StyleColor_HovNodeBorder,    /* original C++ signature */
    hov_node_border = enum.auto()  # (= 4)
    # StyleColor_SelNodeBorder,    /* original C++ signature */
    sel_node_border = enum.auto()  # (= 5)
    # StyleColor_NodeSelRect,    /* original C++ signature */
    node_sel_rect = enum.auto()  # (= 6)
    # StyleColor_NodeSelRectBorder,    /* original C++ signature */
    node_sel_rect_border = enum.auto()  # (= 7)
    # StyleColor_HovLinkBorder,    /* original C++ signature */
    hov_link_border = enum.auto()  # (= 8)
    # StyleColor_SelLinkBorder,    /* original C++ signature */
    sel_link_border = enum.auto()  # (= 9)
    # StyleColor_HighlightLinkBorder,    /* original C++ signature */
    highlight_link_border = enum.auto()  # (= 10)
    # StyleColor_LinkSelRect,    /* original C++ signature */
    link_sel_rect = enum.auto()  # (= 11)
    # StyleColor_LinkSelRectBorder,    /* original C++ signature */
    link_sel_rect_border = enum.auto()  # (= 12)
    # StyleColor_PinRect,    /* original C++ signature */
    pin_rect = enum.auto()  # (= 13)
    # StyleColor_PinRectBorder,    /* original C++ signature */
    pin_rect_border = enum.auto()  # (= 14)
    # StyleColor_Flow,    /* original C++ signature */
    flow = enum.auto()  # (= 15)
    # StyleColor_FlowMarker,    /* original C++ signature */
    flow_marker = enum.auto()  # (= 16)
    # StyleColor_GroupBg,    /* original C++ signature */
    group_bg = enum.auto()  # (= 17)
    # StyleColor_GroupBorder,    /* original C++ signature */
    group_border = enum.auto()  # (= 18)

    # StyleColor_Count    /* original C++ signature */
    # }
    count = enum.auto()  # (= 19)

class StyleVar(enum.Enum):  # imgui_node_editor.h:150
    # StyleVar_NodePadding,    /* original C++ signature */
    node_padding = enum.auto()  # (= 0)
    # StyleVar_NodeRounding,    /* original C++ signature */
    node_rounding = enum.auto()  # (= 1)
    # StyleVar_NodeBorderWidth,    /* original C++ signature */
    node_border_width = enum.auto()  # (= 2)
    # StyleVar_HoveredNodeBorderWidth,    /* original C++ signature */
    hovered_node_border_width = enum.auto()  # (= 3)
    # StyleVar_SelectedNodeBorderWidth,    /* original C++ signature */
    selected_node_border_width = enum.auto()  # (= 4)
    # StyleVar_PinRounding,    /* original C++ signature */
    pin_rounding = enum.auto()  # (= 5)
    # StyleVar_PinBorderWidth,    /* original C++ signature */
    pin_border_width = enum.auto()  # (= 6)
    # StyleVar_LinkStrength,    /* original C++ signature */
    link_strength = enum.auto()  # (= 7)
    # StyleVar_SourceDirection,    /* original C++ signature */
    source_direction = enum.auto()  # (= 8)
    # StyleVar_TargetDirection,    /* original C++ signature */
    target_direction = enum.auto()  # (= 9)
    # StyleVar_ScrollDuration,    /* original C++ signature */
    scroll_duration = enum.auto()  # (= 10)
    # StyleVar_FlowMarkerDistance,    /* original C++ signature */
    flow_marker_distance = enum.auto()  # (= 11)
    # StyleVar_FlowSpeed,    /* original C++ signature */
    flow_speed = enum.auto()  # (= 12)
    # StyleVar_FlowDuration,    /* original C++ signature */
    flow_duration = enum.auto()  # (= 13)
    # StyleVar_PivotAlignment,    /* original C++ signature */
    pivot_alignment = enum.auto()  # (= 14)
    # StyleVar_PivotSize,    /* original C++ signature */
    pivot_size = enum.auto()  # (= 15)
    # StyleVar_PivotScale,    /* original C++ signature */
    pivot_scale = enum.auto()  # (= 16)
    # StyleVar_PinCorners,    /* original C++ signature */
    pin_corners = enum.auto()  # (= 17)
    # StyleVar_PinRadius,    /* original C++ signature */
    pin_radius = enum.auto()  # (= 18)
    # StyleVar_PinArrowSize,    /* original C++ signature */
    pin_arrow_size = enum.auto()  # (= 19)
    # StyleVar_PinArrowWidth,    /* original C++ signature */
    pin_arrow_width = enum.auto()  # (= 20)
    # StyleVar_GroupRounding,    /* original C++ signature */
    group_rounding = enum.auto()  # (= 21)
    # StyleVar_GroupBorderWidth,    /* original C++ signature */
    group_border_width = enum.auto()  # (= 22)
    # StyleVar_HighlightConnectedLinks,    /* original C++ signature */
    highlight_connected_links = enum.auto()  # (= 23)
    # StyleVar_SnapLinkToPinDir,    /* original C++ signature */
    snap_link_to_pin_dir = enum.auto()  # (= 24)
    # StyleVar_HoveredNodeBorderOffset,    /* original C++ signature */
    hovered_node_border_offset = enum.auto()  # (= 25)
    # StyleVar_SelectedNodeBorderOffset,    /* original C++ signature */
    selected_node_border_offset = enum.auto()  # (= 26)

    # StyleVar_Count    /* original C++ signature */
    # }
    count = enum.auto()  # (= 27)

class Style:  # imgui_node_editor.h:183
    # ImVec4  NodePadding;    /* original C++ signature */
    node_padding: ImVec4  # imgui_node_editor.h:185
    # float   NodeRounding;    /* original C++ signature */
    node_rounding: float  # imgui_node_editor.h:186
    # float   NodeBorderWidth;    /* original C++ signature */
    node_border_width: float  # imgui_node_editor.h:187
    # float   HoveredNodeBorderWidth;    /* original C++ signature */
    hovered_node_border_width: float  # imgui_node_editor.h:188
    # float   HoverNodeBorderOffset;    /* original C++ signature */
    hover_node_border_offset: float  # imgui_node_editor.h:189
    # float   SelectedNodeBorderWidth;    /* original C++ signature */
    selected_node_border_width: float  # imgui_node_editor.h:190
    # float   SelectedNodeBorderOffset;    /* original C++ signature */
    selected_node_border_offset: float  # imgui_node_editor.h:191
    # float   PinRounding;    /* original C++ signature */
    pin_rounding: float  # imgui_node_editor.h:192
    # float   PinBorderWidth;    /* original C++ signature */
    pin_border_width: float  # imgui_node_editor.h:193
    # float   LinkStrength;    /* original C++ signature */
    link_strength: float  # imgui_node_editor.h:194
    # ImVec2  SourceDirection;    /* original C++ signature */
    source_direction: ImVec2  # imgui_node_editor.h:195
    # ImVec2  TargetDirection;    /* original C++ signature */
    target_direction: ImVec2  # imgui_node_editor.h:196
    # float   ScrollDuration;    /* original C++ signature */
    scroll_duration: float  # imgui_node_editor.h:197
    # float   FlowMarkerDistance;    /* original C++ signature */
    flow_marker_distance: float  # imgui_node_editor.h:198
    # float   FlowSpeed;    /* original C++ signature */
    flow_speed: float  # imgui_node_editor.h:199
    # float   FlowDuration;    /* original C++ signature */
    flow_duration: float  # imgui_node_editor.h:200
    # ImVec2  PivotAlignment;    /* original C++ signature */
    pivot_alignment: ImVec2  # imgui_node_editor.h:201
    # ImVec2  PivotSize;    /* original C++ signature */
    pivot_size: ImVec2  # imgui_node_editor.h:202
    # ImVec2  PivotScale;    /* original C++ signature */
    pivot_scale: ImVec2  # imgui_node_editor.h:203
    # float   PinCorners;    /* original C++ signature */
    pin_corners: float  # imgui_node_editor.h:204
    # float   PinRadius;    /* original C++ signature */
    pin_radius: float  # imgui_node_editor.h:205
    # float   PinArrowSize;    /* original C++ signature */
    pin_arrow_size: float  # imgui_node_editor.h:206
    # float   PinArrowWidth;    /* original C++ signature */
    pin_arrow_width: float  # imgui_node_editor.h:207
    # float   GroupRounding;    /* original C++ signature */
    group_rounding: float  # imgui_node_editor.h:208
    # float   GroupBorderWidth;    /* original C++ signature */
    group_border_width: float  # imgui_node_editor.h:209
    # float   HighlightConnectedLinks;    /* original C++ signature */
    highlight_connected_links: float  # imgui_node_editor.h:210
    # float   SnapLinkToPinDir;    /* original C++ signature */
    snap_link_to_pin_dir: float  # when True link will start on the line defined by pin direction    # imgui_node_editor.h:211

    # Style()    /* original C++ signature */
    #     {
    #         NodePadding              = ImVec4(8, 8, 8, 8);
    #         NodeRounding             = 12.0f;
    #         NodeBorderWidth          = 1.5f;
    #         HoveredNodeBorderWidth   = 3.5f;
    #         HoverNodeBorderOffset    = 0.0f;
    #         SelectedNodeBorderWidth  = 3.5f;
    #         SelectedNodeBorderOffset = 0.0f;
    #         PinRounding              = 4.0f;
    #         PinBorderWidth           = 0.0f;
    #         LinkStrength             = 100.0f;
    #         SourceDirection          = ImVec2(1.0f, 0.0f);
    #         TargetDirection          = ImVec2(-1.0f, 0.0f);
    #         ScrollDuration           = 0.35f;
    #         FlowMarkerDistance       = 30.0f;
    #         FlowSpeed                = 150.0f;
    #         FlowDuration             = 2.0f;
    #         PivotAlignment           = ImVec2(0.5f, 0.5f);
    #         PivotSize                = ImVec2(0.0f, 0.0f);
    #         PivotScale               = ImVec2(1, 1);
    #                                     #if IMGUI_VERSION_NUM > 18101
    #         PinCorners               = ImDrawFlags_RoundCornersAll;
    #                                     #else
    #         PinCorners               = ImDrawCornerFlags_All;
    #                                     #endif
    #         PinRadius                = 0.0f;
    #         PinArrowSize             = 0.0f;
    #         PinArrowWidth            = 0.0f;
    #         GroupRounding            = 6.0f;
    #         GroupBorderWidth         = 1.0f;
    #         HighlightConnectedLinks  = 0.0f;
    #         SnapLinkToPinDir         = 0.0f;
    # // _SRCML_EMPTY_LINE_
    #         Colors[StyleColor_Bg]                 = ImColor( 60,  60,  70, 200);
    #         Colors[StyleColor_Grid]               = ImColor(120, 120, 120,  40);
    #         Colors[StyleColor_NodeBg]             = ImColor( 32,  32,  32, 200);
    #         Colors[StyleColor_NodeBorder]         = ImColor(255, 255, 255,  96);
    #         Colors[StyleColor_HovNodeBorder]      = ImColor( 50, 176, 255, 255);
    #         Colors[StyleColor_SelNodeBorder]      = ImColor(255, 176,  50, 255);
    #         Colors[StyleColor_NodeSelRect]        = ImColor(  5, 130, 255,  64);
    #         Colors[StyleColor_NodeSelRectBorder]  = ImColor(  5, 130, 255, 128);
    #         Colors[StyleColor_HovLinkBorder]      = ImColor( 50, 176, 255, 255);
    #         Colors[StyleColor_SelLinkBorder]      = ImColor(255, 176,  50, 255);
    #         Colors[StyleColor_HighlightLinkBorder]= ImColor(204, 105,   0, 255);
    #         Colors[StyleColor_LinkSelRect]        = ImColor(  5, 130, 255,  64);
    #         Colors[StyleColor_LinkSelRectBorder]  = ImColor(  5, 130, 255, 128);
    #         Colors[StyleColor_PinRect]            = ImColor( 60, 180, 255, 100);
    #         Colors[StyleColor_PinRectBorder]      = ImColor( 60, 180, 255, 128);
    #         Colors[StyleColor_Flow]               = ImColor(255, 128,  64, 255);
    #         Colors[StyleColor_FlowMarker]         = ImColor(255, 128,  64, 255);
    #         Colors[StyleColor_GroupBg]            = ImColor(  0,   0,   0, 160);
    #         Colors[StyleColor_GroupBorder]        = ImColor(255, 255, 255,  32);
    #     }
    def __init__(self) -> None:  # imgui_node_editor.h:214
        pass

# ------------------------------------------------------------------------------
# void SetCurrentEditor(EditorContext* ctx);    /* original C++ signature */
def set_current_editor(ctx: EditorContext) -> None:  # imgui_node_editor.h:276
    pass

# EditorContext* GetCurrentEditor();    /* original C++ signature */
def get_current_editor() -> EditorContext:  # imgui_node_editor.h:277
    pass

# EditorContext* CreateEditor(const Config* config = nullptr);    /* original C++ signature */
def create_editor(
    config: Optional[Config] = None,
) -> EditorContext:  # imgui_node_editor.h:278
    pass

# void DestroyEditor(EditorContext* ctx);    /* original C++ signature */
def destroy_editor(ctx: EditorContext) -> None:  # imgui_node_editor.h:279
    pass

# const Config& GetConfig(EditorContext* ctx = nullptr);    /* original C++ signature */
def get_config(
    ctx: Optional[EditorContext] = None,
) -> Config:  # imgui_node_editor.h:280
    pass

# Style& GetStyle();    /* original C++ signature */
def get_style() -> Style:  # imgui_node_editor.h:282
    pass

# const char* GetStyleColorName(StyleColor colorIndex);    /* original C++ signature */
def get_style_color_name(color_index: StyleColor) -> str:  # imgui_node_editor.h:283
    pass

# void PushStyleColor(StyleColor colorIndex, const ImVec4& color);    /* original C++ signature */
def push_style_color(
    color_index: StyleColor, color: ImVec4
) -> None:  # imgui_node_editor.h:285
    pass

# void PopStyleColor(int count = 1);    /* original C++ signature */
def pop_style_color(count: int = 1) -> None:  # imgui_node_editor.h:286
    pass

# void PushStyleVar(StyleVar varIndex, float value);    /* original C++ signature */
def push_style_var(
    var_index: StyleVar, value: float
) -> None:  # imgui_node_editor.h:288
    pass

# void PushStyleVar(StyleVar varIndex, const ImVec2& value);    /* original C++ signature */
def push_style_var(
    var_index: StyleVar, value: ImVec2
) -> None:  # imgui_node_editor.h:289
    pass

# void PushStyleVar(StyleVar varIndex, const ImVec4& value);    /* original C++ signature */
def push_style_var(
    var_index: StyleVar, value: ImVec4
) -> None:  # imgui_node_editor.h:290
    pass

# void PopStyleVar(int count = 1);    /* original C++ signature */
def pop_style_var(count: int = 1) -> None:  # imgui_node_editor.h:291
    pass

# void Begin(const char* id, const ImVec2& size = ImVec2(0, 0));    /* original C++ signature */
def begin(id: str, size: ImVec2 = ImVec2(0, 0)) -> None:  # imgui_node_editor.h:293
    pass

# void End();    /* original C++ signature */
def end() -> None:  # imgui_node_editor.h:294
    pass

# void BeginNode(NodeId id);    /* original C++ signature */
def begin_node(id: NodeId) -> None:  # imgui_node_editor.h:296
    pass

# void BeginPin(PinId id, PinKind kind);    /* original C++ signature */
def begin_pin(id: PinId, kind: PinKind) -> None:  # imgui_node_editor.h:297
    pass

# void PinRect(const ImVec2& a, const ImVec2& b);    /* original C++ signature */
def pin_rect(a: ImVec2, b: ImVec2) -> None:  # imgui_node_editor.h:298
    pass

# void PinPivotRect(const ImVec2& a, const ImVec2& b);    /* original C++ signature */
def pin_pivot_rect(a: ImVec2, b: ImVec2) -> None:  # imgui_node_editor.h:299
    pass

# void PinPivotSize(const ImVec2& size);    /* original C++ signature */
def pin_pivot_size(size: ImVec2) -> None:  # imgui_node_editor.h:300
    pass

# void PinPivotScale(const ImVec2& scale);    /* original C++ signature */
def pin_pivot_scale(scale: ImVec2) -> None:  # imgui_node_editor.h:301
    pass

# void PinPivotAlignment(const ImVec2& alignment);    /* original C++ signature */
def pin_pivot_alignment(alignment: ImVec2) -> None:  # imgui_node_editor.h:302
    pass

# void EndPin();    /* original C++ signature */
def end_pin() -> None:  # imgui_node_editor.h:303
    pass

# void Group(const ImVec2& size);    /* original C++ signature */
def group(size: ImVec2) -> None:  # imgui_node_editor.h:304
    pass

# void EndNode();    /* original C++ signature */
def end_node() -> None:  # imgui_node_editor.h:305
    pass

# bool BeginGroupHint(NodeId nodeId);    /* original C++ signature */
def begin_group_hint(node_id: NodeId) -> bool:  # imgui_node_editor.h:307
    pass

# ImVec2 GetGroupMin();    /* original C++ signature */
def get_group_min() -> ImVec2:  # imgui_node_editor.h:308
    pass

# ImVec2 GetGroupMax();    /* original C++ signature */
def get_group_max() -> ImVec2:  # imgui_node_editor.h:309
    pass

# ImDrawList* GetHintForegroundDrawList();    /* original C++ signature */
def get_hint_foreground_draw_list() -> ImDrawList:  # imgui_node_editor.h:310
    pass

# ImDrawList* GetHintBackgroundDrawList();    /* original C++ signature */
def get_hint_background_draw_list() -> ImDrawList:  # imgui_node_editor.h:311
    pass

# void EndGroupHint();    /* original C++ signature */
def end_group_hint() -> None:  # imgui_node_editor.h:312
    pass

# ImDrawList* GetNodeBackgroundDrawList(NodeId nodeId);    /* original C++ signature */
def get_node_background_draw_list(
    node_id: NodeId,
) -> ImDrawList:  # imgui_node_editor.h:315
    """TODO: Add a way to manage node background channels"""
    pass

# bool Link(LinkId id, PinId startPinId, PinId endPinId, const ImVec4& color = ImVec4(1, 1, 1, 1), float thickness = 1.0f);    /* original C++ signature */
def link(  # imgui_node_editor.h:317
    id: LinkId,
    start_pin_id: PinId,
    end_pin_id: PinId,
    color: ImVec4 = ImVec4(1, 1, 1, 1),
    thickness: float = 1.0,
) -> bool:
    pass

# void Flow(LinkId linkId, FlowDirection direction = FlowDirection::Forward);    /* original C++ signature */
def flow(  # imgui_node_editor.h:319
    link_id: LinkId, direction: FlowDirection = FlowDirection.forward
) -> None:
    pass

# bool BeginCreate(const ImVec4& color = ImVec4(1, 1, 1, 1), float thickness = 1.0f);    /* original C++ signature */
def begin_create(  # imgui_node_editor.h:321
    color: ImVec4 = ImVec4(1, 1, 1, 1), thickness: float = 1.0
) -> bool:
    pass

# bool QueryNewLink(PinId* startId, PinId* endId);    /* original C++ signature */
def query_new_link(start_id: PinId, end_id: PinId) -> bool:  # imgui_node_editor.h:322
    pass

# bool QueryNewLink(PinId* startId, PinId* endId, const ImVec4& color, float thickness = 1.0f);    /* original C++ signature */
def query_new_link(  # imgui_node_editor.h:323
    start_id: PinId, end_id: PinId, color: ImVec4, thickness: float = 1.0
) -> bool:
    pass

# bool QueryNewNode(PinId* pinId);    /* original C++ signature */
def query_new_node(pin_id: PinId) -> bool:  # imgui_node_editor.h:324
    pass

# bool QueryNewNode(PinId* pinId, const ImVec4& color, float thickness = 1.0f);    /* original C++ signature */
def query_new_node(  # imgui_node_editor.h:325
    pin_id: PinId, color: ImVec4, thickness: float = 1.0
) -> bool:
    pass

# bool AcceptNewItem();    /* original C++ signature */
def accept_new_item() -> bool:  # imgui_node_editor.h:326
    pass

# bool AcceptNewItem(const ImVec4& color, float thickness = 1.0f);    /* original C++ signature */
def accept_new_item(
    color: ImVec4, thickness: float = 1.0
) -> bool:  # imgui_node_editor.h:327
    pass

# void RejectNewItem();    /* original C++ signature */
def reject_new_item() -> None:  # imgui_node_editor.h:328
    pass

# void RejectNewItem(const ImVec4& color, float thickness = 1.0f);    /* original C++ signature */
def reject_new_item(
    color: ImVec4, thickness: float = 1.0
) -> None:  # imgui_node_editor.h:329
    pass

# void EndCreate();    /* original C++ signature */
def end_create() -> None:  # imgui_node_editor.h:330
    pass

# bool BeginDelete();    /* original C++ signature */
def begin_delete() -> bool:  # imgui_node_editor.h:332
    pass

# bool QueryDeletedLink(LinkId* linkId, PinId* startId = nullptr, PinId* endId = nullptr);    /* original C++ signature */
def query_deleted_link(  # imgui_node_editor.h:333
    link_id: LinkId, start_id: Optional[PinId] = None, end_id: Optional[PinId] = None
) -> bool:
    pass

# bool QueryDeletedNode(NodeId* nodeId);    /* original C++ signature */
def query_deleted_node(node_id: NodeId) -> bool:  # imgui_node_editor.h:334
    pass

# bool AcceptDeletedItem(bool deleteDependencies = true);    /* original C++ signature */
def accept_deleted_item(
    delete_dependencies: bool = True,
) -> bool:  # imgui_node_editor.h:335
    pass

# void RejectDeletedItem();    /* original C++ signature */
def reject_deleted_item() -> None:  # imgui_node_editor.h:336
    pass

# void EndDelete();    /* original C++ signature */
def end_delete() -> None:  # imgui_node_editor.h:337
    pass

# void SetNodePosition(NodeId nodeId, const ImVec2& editorPosition);    /* original C++ signature */
def set_node_position(
    node_id: NodeId, editor_position: ImVec2
) -> None:  # imgui_node_editor.h:339
    pass

# void SetGroupSize(NodeId nodeId, const ImVec2& size);    /* original C++ signature */
def set_group_size(node_id: NodeId, size: ImVec2) -> None:  # imgui_node_editor.h:340
    pass

# ImVec2 GetNodePosition(NodeId nodeId);    /* original C++ signature */
def get_node_position(node_id: NodeId) -> ImVec2:  # imgui_node_editor.h:341
    pass

# ImVec2 GetNodeSize(NodeId nodeId);    /* original C++ signature */
def get_node_size(node_id: NodeId) -> ImVec2:  # imgui_node_editor.h:342
    pass

# void CenterNodeOnScreen(NodeId nodeId);    /* original C++ signature */
def center_node_on_screen(node_id: NodeId) -> None:  # imgui_node_editor.h:343
    pass

# void SetNodeZPosition(NodeId nodeId, float z);     /* original C++ signature */
def set_node_z_position(node_id: NodeId, z: float) -> None:  # imgui_node_editor.h:344
    """Sets node z position, nodes with higher value are drawn over nodes with lower value"""
    pass

# float GetNodeZPosition(NodeId nodeId);     /* original C++ signature */
def get_node_z_position(node_id: NodeId) -> float:  # imgui_node_editor.h:345
    """Returns node z position, defaults is 0.0"""
    pass

# void RestoreNodeState(NodeId nodeId);    /* original C++ signature */
def restore_node_state(node_id: NodeId) -> None:  # imgui_node_editor.h:347
    pass

# void Suspend();    /* original C++ signature */
def suspend() -> None:  # imgui_node_editor.h:349
    pass

# void Resume();    /* original C++ signature */
def resume() -> None:  # imgui_node_editor.h:350
    pass

# bool IsSuspended();    /* original C++ signature */
def is_suspended() -> bool:  # imgui_node_editor.h:351
    pass

# bool IsActive();    /* original C++ signature */
def is_active() -> bool:  # imgui_node_editor.h:353
    pass

# bool HasSelectionChanged();    /* original C++ signature */
def has_selection_changed() -> bool:  # imgui_node_editor.h:355
    pass

# int  GetSelectedObjectCount();    /* original C++ signature */
def get_selected_object_count() -> int:  # imgui_node_editor.h:356
    pass

# int  GetSelectedNodes(NodeId* nodes, int size);    /* original C++ signature */
def get_selected_nodes(nodes: NodeId, size: int) -> int:  # imgui_node_editor.h:357
    pass

# int  GetSelectedLinks(LinkId* links, int size);    /* original C++ signature */
def get_selected_links(links: LinkId, size: int) -> int:  # imgui_node_editor.h:358
    pass

# bool IsNodeSelected(NodeId nodeId);    /* original C++ signature */
def is_node_selected(node_id: NodeId) -> bool:  # imgui_node_editor.h:359
    pass

# bool IsLinkSelected(LinkId linkId);    /* original C++ signature */
def is_link_selected(link_id: LinkId) -> bool:  # imgui_node_editor.h:360
    pass

# void ClearSelection();    /* original C++ signature */
def clear_selection() -> None:  # imgui_node_editor.h:361
    pass

# void SelectNode(NodeId nodeId, bool append = false);    /* original C++ signature */
def select_node(
    node_id: NodeId, append: bool = False
) -> None:  # imgui_node_editor.h:362
    pass

# void SelectLink(LinkId linkId, bool append = false);    /* original C++ signature */
def select_link(
    link_id: LinkId, append: bool = False
) -> None:  # imgui_node_editor.h:363
    pass

# void DeselectNode(NodeId nodeId);    /* original C++ signature */
def deselect_node(node_id: NodeId) -> None:  # imgui_node_editor.h:364
    pass

# void DeselectLink(LinkId linkId);    /* original C++ signature */
def deselect_link(link_id: LinkId) -> None:  # imgui_node_editor.h:365
    pass

# bool DeleteNode(NodeId nodeId);    /* original C++ signature */
def delete_node(node_id: NodeId) -> bool:  # imgui_node_editor.h:367
    pass

# bool DeleteLink(LinkId linkId);    /* original C++ signature */
def delete_link(link_id: LinkId) -> bool:  # imgui_node_editor.h:368
    pass

# bool HasAnyLinks(NodeId nodeId);     /* original C++ signature */
def has_any_links(node_id: NodeId) -> bool:  # imgui_node_editor.h:370
    """Returns True if node has any link connected"""
    pass

# bool HasAnyLinks(PinId pinId);     /* original C++ signature */
def has_any_links(pin_id: PinId) -> bool:  # imgui_node_editor.h:371
    """Return True if pin has any link connected"""
    pass

# int BreakLinks(NodeId nodeId);     /* original C++ signature */
def break_links(node_id: NodeId) -> int:  # imgui_node_editor.h:372
    """Break all links connected to this node"""
    pass

# int BreakLinks(PinId pinId);     /* original C++ signature */
def break_links(pin_id: PinId) -> int:  # imgui_node_editor.h:373
    """Break all links connected to this pin"""
    pass

# void NavigateToContent(float duration = -1);    /* original C++ signature */
def navigate_to_content(duration: float = -1) -> None:  # imgui_node_editor.h:375
    pass

# void NavigateToSelection(bool zoomIn = false, float duration = -1);    /* original C++ signature */
def navigate_to_selection(
    zoom_in: bool = False, duration: float = -1
) -> None:  # imgui_node_editor.h:376
    pass

# bool ShowNodeContextMenu(NodeId* nodeId);    /* original C++ signature */
def show_node_context_menu(node_id: NodeId) -> bool:  # imgui_node_editor.h:378
    pass

# bool ShowPinContextMenu(PinId* pinId);    /* original C++ signature */
def show_pin_context_menu(pin_id: PinId) -> bool:  # imgui_node_editor.h:379
    pass

# bool ShowLinkContextMenu(LinkId* linkId);    /* original C++ signature */
def show_link_context_menu(link_id: LinkId) -> bool:  # imgui_node_editor.h:380
    pass

# bool ShowBackgroundContextMenu();    /* original C++ signature */
def show_background_context_menu() -> bool:  # imgui_node_editor.h:381
    pass

# void EnableShortcuts(bool enable);    /* original C++ signature */
def enable_shortcuts(enable: bool) -> None:  # imgui_node_editor.h:383
    pass

# bool AreShortcutsEnabled();    /* original C++ signature */
def are_shortcuts_enabled() -> bool:  # imgui_node_editor.h:384
    pass

# bool BeginShortcut();    /* original C++ signature */
def begin_shortcut() -> bool:  # imgui_node_editor.h:386
    pass

# bool AcceptCut();    /* original C++ signature */
def accept_cut() -> bool:  # imgui_node_editor.h:387
    pass

# bool AcceptCopy();    /* original C++ signature */
def accept_copy() -> bool:  # imgui_node_editor.h:388
    pass

# bool AcceptPaste();    /* original C++ signature */
def accept_paste() -> bool:  # imgui_node_editor.h:389
    pass

# bool AcceptDuplicate();    /* original C++ signature */
def accept_duplicate() -> bool:  # imgui_node_editor.h:390
    pass

# bool AcceptCreateNode();    /* original C++ signature */
def accept_create_node() -> bool:  # imgui_node_editor.h:391
    pass

# int  GetActionContextSize();    /* original C++ signature */
def get_action_context_size() -> int:  # imgui_node_editor.h:392
    pass

# int  GetActionContextNodes(NodeId* nodes, int size);    /* original C++ signature */
def get_action_context_nodes(
    nodes: NodeId, size: int
) -> int:  # imgui_node_editor.h:393
    pass

# int  GetActionContextLinks(LinkId* links, int size);    /* original C++ signature */
def get_action_context_links(
    links: LinkId, size: int
) -> int:  # imgui_node_editor.h:394
    pass

# void EndShortcut();    /* original C++ signature */
def end_shortcut() -> None:  # imgui_node_editor.h:395
    pass

# float GetCurrentZoom();    /* original C++ signature */
def get_current_zoom() -> float:  # imgui_node_editor.h:397
    pass

# NodeId GetHoveredNode();    /* original C++ signature */
def get_hovered_node() -> NodeId:  # imgui_node_editor.h:399
    pass

# PinId GetHoveredPin();    /* original C++ signature */
def get_hovered_pin() -> PinId:  # imgui_node_editor.h:400
    pass

# LinkId GetHoveredLink();    /* original C++ signature */
def get_hovered_link() -> LinkId:  # imgui_node_editor.h:401
    pass

# NodeId GetDoubleClickedNode();    /* original C++ signature */
def get_double_clicked_node() -> NodeId:  # imgui_node_editor.h:402
    pass

# PinId GetDoubleClickedPin();    /* original C++ signature */
def get_double_clicked_pin() -> PinId:  # imgui_node_editor.h:403
    pass

# LinkId GetDoubleClickedLink();    /* original C++ signature */
def get_double_clicked_link() -> LinkId:  # imgui_node_editor.h:404
    pass

# bool IsBackgroundClicked();    /* original C++ signature */
def is_background_clicked() -> bool:  # imgui_node_editor.h:405
    pass

# bool IsBackgroundDoubleClicked();    /* original C++ signature */
def is_background_double_clicked() -> bool:  # imgui_node_editor.h:406
    pass

# ImGuiMouseButton GetBackgroundClickButtonIndex();     /* original C++ signature */
def get_background_click_button_index() -> ImGuiMouseButton:  # imgui_node_editor.h:407
    """-1 if none"""
    pass

# ImGuiMouseButton GetBackgroundDoubleClickButtonIndex();     /* original C++ signature */
def get_background_double_click_button_index() -> ImGuiMouseButton:  # imgui_node_editor.h:408
    """-1 if none"""
    pass

# bool GetLinkPins(LinkId linkId, PinId* startPinId, PinId* endPinId);     /* original C++ signature */
def get_link_pins(  # imgui_node_editor.h:410
    link_id: LinkId, start_pin_id: PinId, end_pin_id: PinId
) -> bool:
    """pass None if particular pin do not interest you"""
    pass

# bool PinHadAnyLinks(PinId pinId);    /* original C++ signature */
def pin_had_any_links(pin_id: PinId) -> bool:  # imgui_node_editor.h:412
    pass

# ImVec2 GetScreenSize();    /* original C++ signature */
def get_screen_size() -> ImVec2:  # imgui_node_editor.h:414
    pass

# ImVec2 ScreenToCanvas(const ImVec2& pos);    /* original C++ signature */
def screen_to_canvas(pos: ImVec2) -> ImVec2:  # imgui_node_editor.h:415
    pass

# ImVec2 CanvasToScreen(const ImVec2& pos);    /* original C++ signature */
def canvas_to_screen(pos: ImVec2) -> ImVec2:  # imgui_node_editor.h:416
    pass

# int GetNodeCount();                                    /* original C++ signature */
def get_node_count() -> int:  # imgui_node_editor.h:418
    """Returns number of submitted nodes since Begin() call"""
    pass

# int GetOrderedNodeIds(NodeId* nodes, int size);        /* original C++ signature */
def get_ordered_node_ids(nodes: NodeId, size: int) -> int:  # imgui_node_editor.h:419
    """Fills an array with node id's in order they're drawn; up to 'size` elements are set. Returns actual size of filled id's."""
    pass

# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------

# namespace ax

# ------------------------------------------------------------------------------
# # endif
####################    </generated_from:imgui_node_editor.h>    ####################

# </litgen_stub> // Autogenerated code end!