# 编排
在大模型应用开发中，我们需要将各种基础组件，比如ChatModel，Embedding，ToolsNode ，Reriever等，按照业务逻辑进行组合串联，最终完成特定的功能，这种就是编排。

Eino框架提供了一套强大的编排功能，包括Chain、Graph和Workflow三种编排方式

# Chain
Chain 可以视为是 Graph 的简化封装


# Graph
Graph是Eino中最基础、最强大的编排方式，它基于节点（Node）和边（Edge）的模型，可以绘制出复杂的数据流动网络，支持分支、并行、循环等复杂结构。

# Workflow
Workflow提供了字段级别的映射能力，可以将不同节点的输出字段灵活地映射到其他节点的输入字段。


* 与 Graph API 具有同等级别的能力，都是编排“围绕大模型的信息流”的合适框架工具。
  * 在节点类型、流处理、callback、option、state、interrupt & checkpoint 等方面保持一致。
  * 实现 AnyGraph 接口，可以在 AddGraphNode 时作为子图加入上级 Graph/Chain/Workflow。
  * 也可以把其他 Graph/Chain/Workflow 添加为自己的子图。
* 字段级别映射能力：节点的输入可以由任意前驱节点的任意输出字段组合而成。
  * 原生支持 struct，map 以及任意嵌套层级的 struct 和 map 之间的相互映射。
* 控制流与数据流分离：Graph 的 Edge 是既决定执行顺序，又决定数据传递。Workflow 中可以一起传递，也可以分开传递。
* 不支持环（即类似 react agent 的 chatmodel->toolsNode->chatmodel 的环路）。NodeTriggerMode 固定为 AllPredecessor