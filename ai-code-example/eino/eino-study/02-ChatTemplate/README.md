ChatTemplate 支持多种模板化方式，最常见的包括：

FString 格式：使用 {variable} 语法进行变量替换
GoTemplate 格式：使用 Go 标准库的 text/template 语法，支持条件判断、循环等复杂逻辑
Jinja2 格式：使用 Jinja2 模板语法


History 格式：支持在模板中包含历史消息，用于实现上下文感知的对话