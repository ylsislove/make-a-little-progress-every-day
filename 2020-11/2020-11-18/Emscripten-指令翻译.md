# Emscripten-指令翻译

- [`-O0`](#-o0)
- [`-O1`](#-o1)
- [`-O2`](#-o2)
- [`-O3`](#-o3)
- [`-Os`](#-os)
- [`-Oz`](#-oz)
- [`-s OPTION[=VALUE]`](#-s-optionvalue)
- [`-g`](#-g)
- [`-gseparate-dwarf[=FILENAME]`](#-gseparate-dwarffilename)
- [`-g<level>`](#-glevel)
- [`--profiling`](#--profiling)
- [`--profiling-funcs`](#--profiling-funcs)
- [`-tracing`](#-tracing)
- [`--emit-symbol-map`](#--emit-symbol-map)
- [`--llvm-opts <level>`](#--llvm-opts-level)
- [`-flto`](#-flto)
- [`--closure <on>`](#--closure-on)
- [`-pre-js <file>`](#-pre-js-file)
- [`--post-js <file>`](#--post-js-file)
- [`--extern-pre-js <file>`](#--extern-pre-js-file)
- [`--extern-post-js <file>`](#--extern-post-js-file)
- [`--embed-file <file>`](#--embed-file-file)
- [`-preload-file <name>`](#-preload-file-name)
- [`--exclud-file <name>`](#--exclud-file-name)
- [`--use-preload-plugins`](#--use-preload-plugins)
- [`-shell-file <path>`](#-shell-file-path)
- [`--source-map-base <base-url>`](#--source-map-base-base-url)
- [`--minify 0`](#--minify-0)
- [`--js-transform <cmd>`](#--js-transform-cmd)
- [`-bind`](#-bind)
- [`--ignore-dynamic-link`](#--ignore-dynamic-link)
- [`--js-library <lib>`](#--js-library-lib)
- [`-v`](#-v)
- [`--cache`](#--cache)
- [`--clear-cache`](#--clear-cache)
- [`--clear-ports`](#--clear-ports)
- [`--show-ports`](#--show-ports)
- [`-memory-init-file <on>`](#-memory-init-file-on)
- [`-Wwarn-absolute-paths`](#-wwarn-absolute-paths)
- [`--proxy-to-worker`](#--proxy-to-worker)
- [`--emrun`](#--emrun)
- [`--cpuprofiler`](#--cpuprofiler)
- [`-memoryprofiler`](#-memoryprofiler)
- [`--threadprofiler`](#--threadprofiler)
- [`--em-config`](#--em-config)
- [`--default-obj-ext .ext`](#--default-obj-ext-ext)
- [`--valid-abspath path`](#--valid-abspath-path)
- [`-o `](#-o-)
- [`-c`](#-c)
- [`--output_eol windows|linux`](#--output_eol-windowslinux)
- [`--cflags`](#--cflags)

Emscripten编译器前端(emcc)
***********************************

Emscripten编译器前端（"emcc"）用于从命令行调用Emscripten编译器。它实际上是标准编译器的替代品，如*gcc*或*clang*。

命令行语法
-------------

   emcc [选项] 文件...

(请注意，如果你想从你当前的目录中运行emcc，你将需要"./emcc"。)

输入文件可以是*Clang*能够处理的源代码文件（C或C++），二进制形式的LLVM位码，或者是人类可读形式的LLVM汇编文件。

参数
---------

大多数clang选项都可以使用，例如gcc选项也可以。      

   显示这些信息

   emcc --help

   显示编译器版本信息

   emcc --version

要查看Emscripten使用的*Clang*版本所支持的*Clang*选项的完整列表，请运行 "clang --help"。

下面列出了在*emcc*中被修改或新增的选项。

### `-O0`
不进行优化 (默认)。这是开始移植一个项目时推荐的设置， 因为它包含了各种断言。

这个设置和其他优化设置在编译和链接过程中都有意义。在编译过程中，它会影响 LLVM 的优化，而在链接过程中，它会影响 Binaryen 中代码的最终优化以及 JS 的优化。 (对于快速增量构建来说，"-O0 "是最好的，而对于发布来说，你应该用更高的东西来链接。)

### `-O1`
简单的优化。在编译步骤中，这些包括LLVM"-O1 "优化。在链接步骤中，这不包括JS中的各种运行时断言，而*-O0*会做。

### `-O2`
像"-O1 "一样，但可以实现更多的优化。在链接过程中，这也将启用各种JavaScript优化。

注意

    这些JavaScript优化可以通过删除编译器看不到的东西来减少代码大小，特别是，如果没有在 "模块 "对象上导出，运行时的部分代码可能会被剥离。编译器知道-pre-js和-post-js中的代码，所以你可以安全地使用那里的运行时。另外，你也可以使用 "EXTRA_EXPORTED_RUNTIME_METHODS"，见 src/settings.js。

### `-O3`
像"-O2 "一样，但有额外的优化，可能需要更长的时间来运行。

注意：这对于发布版构建来说是个不错的设置。

    这对于发布版来说是个很好的设置 This is a good setting for a release build.

### `-Os`
就像"-O3 "一样，但更注重代码的大小（可能会在速度上做出折衷）。这可能会影响wasm和JavaScript。

### `-Oz`
就像"-Os "一样，但会进一步减少代码的大小，并可能需要更长的时间来运行。这对wasm和JavaScript都有影响。

请注意，如果你想了解更多关于优化代码的技巧，请参考优化代码。

    关于优化代码的更多提示，请参见优化代码。

### `-s OPTION[=VALUE]`
Emscripten构建选项。关于可用的选项，请参见 src/settings.js。

注意：你可以在布尔选项前加上 "NO_"来反转它们。

    你可以在布尔选项前加上 "NO_"来反转它们。例如，"-s EXIT_RUNTIME=1 "和"-s NO_EXIT_RUNTIME=0 "是一样的。

注释

    如果没有指定数值，则默认为 "1"。

注意：如果没有指定值，将默认为 "1"。

    对于列表选项，在大多数shell中，你需要在列表周围加上引号("")(以避免出现错误)。下面是两个例子。

    -s RUNTIME_LINKED_LIBS="['liblib.so']"
    -s "RUNTIME_LINKED_LIBS=['liblib.so']"

你也可以指定一个选项的值将从一个指定的JSON格式的文件中读取。例如，下面的选项将 "EXPORTED_FUNCTIONS "选项设置为**path/to/file**的文件内容。

    -s EXPORTED_FUNCTIONS=@/path/to/file

注： * 在这种情况下，文件可能包含一个JSON格式化的函数列表：

    * 在这种情况下，文件可能包含一个JSON格式的函数清单。"["_func1", "func2"]"。

    * 指定的文件路径必须是绝对的，而不是相对的。

注意：选项可以作为单个参数指定。

    选项可以作为一个单一的参数来指定，在"-s "和选项名之间不需要空格，例如"-sFOO=1"。

### `-g`
保留调试信息。

* 当编译到对象文件时，这与*Clang*和*gcc*中的做法相同，它将调试信息添加到对象文件中。

* 当链接时，这相当于-g3。

### `-gseparate-dwarf[=FILENAME]`
保留调试信息，但在旁边的单独文件中。这与"-g "相同，但主文件将不包含调试信息。取而代之的是，调试信息将出现在旁边的一个文件中，如果提供了 "FILENAME"，则与wasm文件相同，但后缀为".debug.wasm"。虽然主文件不包含任何调试信息，但它确实包含了一个指向调试文件所在的URL，以便devtools能够找到它。你可以使用"-s SEPARATE_DWARF_URL=URL "来自定义该位置（例如，如果你想把它托管在不同的服务器上，这很有用）。

### `-g<level>`
控制可调试的级别。每一级都建立在前一级的基础上。

    * "-g0": 不努力保持代码的可调试性 * "-g1"：

    * "-g1": 链接时，保留JavaScript中的空白。

    * "-g2": 链接时，在编译后的代码中保留函数名。 * "-g3"：

    * "-g3": 当编译到对象文件时，保留调试信息，包括JS空白，函数名，以及LLVM调试信息（如果有的话）（这与-g相同）。

    * "-g4": 当链接时，使用LLVM调试信息生成一个源映射（这些信息必须存在于对象文件中，即它们应该是用"-g "编译的）。

    注意： * 源映射允许你查看和使用LLVM调试信息（必须存在于对象文件中，即应该用"-g "编译）。

        源码图允许你在浏览器的调试器中查看和调试*C/C++源代码*！ *这个调试级别可能会使你的程序变得更加复杂。

        * 这个调试级别可能会使编译速度明显变慢（这就是为什么我们只在"-g4 "上这样做）。

### `--profiling`
发出JavaScript时使用合理的默认值，使构建的代码可读，但对剖析仍然有用。这设置了"-g2"（保留空白和函数名），也可以启用影响性能的优化，否则可能无法在"-g2 "中执行。

### `--profiling-funcs`
在剖析中保留函数名，但除此之外，我们通常在优化构建中对空白和名称进行最小化。如果你想根据函数名查看剖析结果，但又不打算*阅读发出的代码，那么这个方法就很有用。

### `-tracing`
启用Emscripten Tracing API。

### `--emit-symbol-map`
在最小化的全局名称和原始函数名称之间保存一个映射文件。例如，这允许您重建有意义的堆栈痕迹。

注意：这只适用于*最小化全局名的情况。

    这只适用于在"-O2 "及以上版本中*最小化全局名的情况，以及没有指定"-g "选项以防止最小化的情况。

### `--llvm-opts <level>`
启用LLVM优化，与我们调用LLVM优化器相关（在将源文件构建为对象文件/位码时进行）。可能的 "级别 "值是： * "0": 启用LLVM优化。

    * "0": 没有LLVM优化（默认为-O0）。

    * "1": LLVM "-O1 "优化（默认为-O1）。

    * "2": LLVM "-O2 "优化.

    * "3": LLVM "-O3 "优化（默认为-O2+）。

你也可以指定任意的LLVM选项，例如： --llvm-opts "-O2 "优化。

    --llvm-opts "['-O3', '-somethingelse']"

一般情况下你不需要指定这个选项，因为"-O "与优化级别会设置一个好的值。

### `-flto`
启用链接时间优化（LTO）。

### `--closure <on>`
运行*Closure Compiler*。可能的 "on "值为

    * "0": 没有关闭编译器（默认值为"-O2 "及以下）。

    * "1": 运行闭包编译器。这将大大减少支持JavaScript代码的大小（除了WebAssembly或asm.js之外的所有代码）。请注意，这将大大增加编译时间。

    * "2": 在*所有*发出的代码上运行闭包编译器，即使是在**asm.js**模式下的**asm.js**输出。这可以进一步减小代码大小，但确实阻止了大量的**asm.js**优化，所以不建议这样做，除非你想不惜一切代价减小代码大小。

注意：*考虑使用"-s MODA"。

    * 当使用closure时，考虑使用"-s MODULARIZE=1"，因为它将globals最小化为可能与全局范围内的其他名称冲突的名称。"MODULARIZE "将所有的输出放到一个函数中（见 "src/settings.js"）。

    * Closure将默认对*Module*本身的名称进行最小化! 使用 "MODULARIZE "也可以解决这个问题。另一个解决方法是确保在闭包编译的代码运行之前，已经存在一个叫做*Module*的全局变量，因为这样它就会重用这个变量。

    * 如果闭包编译器遇到内存不足的情况，可以尝试调整环境中的 "JAVA_HEAP_SIZE"（比如4GB的情况下，调整为4096m）。

    * 只有在进行JavaScript opts时才会运行closure（"-O2 "或以上）。

### `-pre-js <file>`
指定一个文件，其内容被添加在发出的代码之前，并与之一起优化。请注意，这可能不是JS输出中的第一件事，例如，如果使用了 "MODULARIZE"（见 "src/settings.js"）。如果你想这样做，你可以直接预置到emcripten的输出中；"--pre-js "的好处是，它与emcripten输出的其他代码一起优化，可以更好地消除死代码和最小化，它应该只用于这个目的。特别是，"--pre-js "代码不应该改变emcripten的主要输出，以免混淆优化器，比如使用"--pre-js "+"--post-js "把所有的输出都放在一个内部函数范围内（参见 "MODULARIZE"）。

*--pre-js*（但不是*--post-js*）对于在 "Module "对象上指定东西也很有用，因为它出现在JS查看 "Module "之前（例如，你可以在那里定义 "Module['print']"）。

### `--post-js <file>`
和"--pre-js "一样，但在发出代码后发出*个文件。

### `--extern-pre-js <file>`
指定一个文件，该文件的内容被预置到JavaScript输出中。这个文件是在所有其他工作完成之后，包括优化、可选的 "MODULARIZE "化、"SAFE_HEAP "等工具化之后，才被预置到最终的JavaScript输出中。这和在 "emcc "完成运行后预置这个文件是一样的，只是一种方便的方式。相比之下，"--pre-js "和"--post-js "会将代码和其他一切代码一起优化，如果运行*MODULARIZE*，则会将代码保持在同一个范围内，等等）。

### `--extern-post-js <file>`
和"--extern-pre-js "一样，但附加在最后。

### `--embed-file <file>`
指定要嵌入到生成的JavaScript中的文件（带路径）。这个路径是相对于编译时的当前目录而言的。如果这里传递了一个目录，它的全部内容将被嵌入。

例如，如果命令中包含"--embed-file dir/file.dat"，那么 "dir/file.dat "必须相对于你运行*emcc*的目录而存在。

请注意。

    嵌入文件比预加载文件的效率低得多。你应该只对小文件使用它，而且数量不多。取而代之的是使用"--preload-file"，它可以发出高效的二进制数据。

关于"--embed-file "选项的更多信息，请参见打包文件。

### `-preload-file <name>`
在异步运行编译后的代码之前，指定一个要预加载的文件。该路径是相对于编译时的当前目录而言的。如果这里传递了一个目录，它的全部内容将被嵌入。

预加载的文件存储在**filename.data**中，其中**filename.html**是您要编译的主文件。要运行你的代码，你将需要**.html**和**.data**。

注意：这个选项类似于 --embed.html。

    这个选项类似于--embed-file，只是它只在生成HTML（它使用异步的二进制*XHRs*），或者将在网页中使用的JavaScript时才有意义。

*emcc*运行工具/file_packager.py来完成嵌入式和预加载文件的实际打包。如果你想的话，你可以自己运行文件打包器（参见使用文件打包器工具打包）。然后你应该把文件打包器的输出放在emcc"--prejs "中，这样它就会在你的主编译代码之前执行。

关于"--preload-file "选项的更多信息，请参见打包文件。

### `--exclud-file <name>`
要从--embed-file和--preload-file中排除的文件和目录。支持通配符（*）。

### `--use-preload-plugins`
告诉文件打包器在文件加载时对文件运行预加载插件。这将执行一些任务，比如使用浏览器的编解码器对图像和音频进行解码。

### `-shell-file <path>`
生成HTML输出时使用的HTML骨架文件的路径名。所用的shell文件需要有这个标记。"{{{SCRIPT }}}"。

注意：

    * 请参阅 src/shell.html 和 src/shell_minimal.html 的例子。

    * 如果使用"-o "选项指定了HTML以外的目标，这个参数将被忽略。

### `--source-map-base <base-url>`
   WebAssembly源码地图发布的位置的URL。当提供这个选项时，**.wasm**文件会被更新为有 "sourceMappingURL "部分。由此产生的URL将具有以下格式。`<base-url>` + `<wasm-file-name>` + `.map`.

### `--minify 0`
与"-g1 "相同。

### `--js-transform <cmd>`
指定一个`<cmd>`，在生成的代码被优化之前对其进行调用。这让你可以修改JavaScript，例如添加或删除一些代码，这些修改将与生成的代码一起被优化。

`<cmd>`将以生成代码的文件名作为参数进行调用。要修改代码，可以先读取原始数据，然后追加到原始数据上，或者用修改后的数据覆盖。

`<cmd>`被解释为一个以空格分隔的参数列表，例如，**python processor.py**的`<cmd>`将导致一个Python脚本被运行。

### `-bind`
使用Embind绑定编译源代码，连接C/C++和JavaScript。

### `--ignore-dynamic-link`
告诉编译器忽略动态链接（用户以后需要手动链接到共享库）。

通常情况下，*emcc*会简单地从动态库中链接代码，就像静态链接一样，如果同一个动态库被链接超过一次，就会失败。有了这个选项，动态链接就会被忽略，这使得构建系统能够顺利进行，不会出现错误。

### `--js-library <lib>`
除了Emscripten的核心库(src/library_*)之外，还可以使用的JavaScript库。

### `-v`
开启verbose输出。

这将把"-v "传递给*Clang*，同时启用 "EMCC_DEBUG "为编译器的各个阶段生成中间文件。它还将运行Emscripten对工具链的内部卫生性检查等。

小提示

    "emcc -v "是一个诊断错误的有用工具。不管有没有其他参数，它都能发挥作用。

### `--cache`
设置用来作为Emscripten缓存的目录。Emscripten缓存用于存储 "libc"、"libcxx "和其他库的预建版本。

如果与"--clear-cache "结合使用，请务必先指定这个参数。

Emscripten缓存默认为 "emcripten/cache"，但可以使用 "EM_CACHE "环境变量或 "CACHE "配置设置来重写。

### `--clear-cache`
手动清除编译后的Emscripten系统库（libc++、libc++abi、libc）的缓存。

这通常是自动处理的，但如果你在原地更新LLVM（而不是有一个新版本的不同目录），缓存机制可能会变得混乱。清除缓存可以解决与缓存不兼容有关的奇怪问题，比如*Clang*无法与库文件链接。这也会清除其他缓存数据。清除缓存后，这个过程将退出。

默认情况下，这也会清除任何下载端口，因为端口目录通常在缓存目录内。

### `--clear-ports`
手动清除 Emscripten Ports 仓库中的本地 port 副本 (sdl2 等)。这也会清除缓存， 以删除它们的联编版本。

您只需要在出现问题时才需要这样做， 而且您希望所有您使用的 port 都能从头开始下载和联编。在这个操作完成后，这个进程将退出。

### `--show-ports`
显示 Emscripten Ports 仓库中可用项目的列表。在此操作完成后， 这个进程将退出。

### `-memory-init-file <on>`
指定是否要单独发出一个内存初始化文件。

    注意。

    请注意，这只有在不发射wasm时才有意义，因为wasm在wasm二进制中嵌入了内存初始化数据。

可能的 "on "值是

    * "0": 不发送单独的内存初始化文件，而是将静态初始化保存在wasm二进制文件中。
    相反，在生成的JavaScript中以文本形式保留静态初始化。如果使用-O0或-O1链接时间优化标志编译，这是默认设置。

    * "1": 发送一个单独的二进制格式的内存初始化文件。这比将其作为文本存储在JavaScript中更有效，但这意味着你有另一个文件要发布。二进制文件也将被异步加载，这意味着 "main() "不会被调用，直到文件被下载并应用；在它到达之前，你不能调用任何C函数。这是用-O2或更高版本编译时的默认设置。

    注意：在使用-O2或更高版本编译时，这是默认设置。

        确保安全调用C函数（初始化文件已经加载）的最安全方法是在 "main() "中调用一个通知函数。

    注意事项

        如果你给 "Module.memoryInitializerRequest "分配一个网络请求（在脚本运行之前），那么它将使用该请求而不是自动为你开始下载。这样做的好处是，你可以在HTML中，在脚本实际到达之前就启动内存初始化文件的请求。为了达到这个目的，网络请求应该是一个XMLHttpRequest，响应类型设置为"'arraybuffer'"。(你也可以把任何其他对象放在这里，它必须提供一个包含ArrayBuffer的".response "属性。)

### `-Wwarn-absolute-paths`
启用对"-I "和"-L "命令行指令中使用绝对路径的警告。这用来警告无意中使用绝对路径，在引用非可移植的本地系统头文件时，这有时是危险的。

### `--proxy-to-worker`
在 Worker 中运行主应用程序代码，将事件代理到 Worker 中并从 Worker 中输出。如果发出HTML，则会发出一个**.html**文件和一个单独的**.js**文件，其中包含要在Worker中运行的JavaScript。如果发出JavaScript，目标文件名包含要在主线程上运行的部分，而第二个后缀为".worker.js "的**.js**文件将包含worker部分。

### `--emrun`
使生成的输出能够被emrun命令行工具所感知。当通过*emrun*运行生成的应用程序时，允许捕获 "stdout"、"stderr "和 "exit(returncode)"。这样就可以启用*EXIT_RUNTIME=1*，允许正常的运行时退出与返回代码传递）。

### `--cpuprofiler`
在生成的页面上嵌入一个简单的CPU剖析器。用它来执行粗略的交互式性能剖析。

### `-memoryprofiler`
在生成的页面上嵌入一个内存分配跟踪器。用它来描述应用程序对Emscripten HEAP的使用情况。

### `--threadprofiler`
在生成的页面中嵌入一个线程活动分析器。当目标是多线程构建时， 可以用它来分析应用程序对 pthreads 的使用情况 (-s USE_PTHREADS=1/2)。

### `--em-config`
指定**.emcripten**配置文件的位置。如果没有指定，emcripten将首先在emcripten目录下搜索".emcripten"，然后在用户的主目录下搜索("~/.emcripten")。这可以使用 "EM_CONFIG "环境变量来覆盖。

### `--default-obj-ext .ext`
如果目录名的位置被传递给"-o "指令，则指定要生成的文件后缀。

例如，考虑以下命令，默认情况下会生成一个输出名为**dir/a.o**的文件。使用"--default-obj-ext .ext"，生成的文件有自定义后缀*dir/a.ext*。

    emcc -c a.c -o dir/。

### `--valid-abspath path`
注意一个允许的绝对路径，我们不应该对其进行警告（绝对的包含路径通常会被警告，因为它们可能会引用本地系统头文件等，我们在交叉编译时需要避免）。

### `-o `
`<target>`文件名扩展名定义了生成的输出类型为。

    * <name> **.js** .JavaScript（如果是WebAssembly，则单独生成**<name>.wasm**文件）。JavaScript (+单独的**<name>.wasm**文件，如果发射WebAssembly)。(默认)

    * <name> **.mjs** : ES6 JavaScript 模块 (如果发射 WebAssembly，则需要单独的 **<name>.wasm** 文件)。

    <name> **.html** : HTML + 单独的 JavaScript 文件 (**<name>.js**; + 单独的 **<name>.wasm** 文件，如果使用 WebAssembly)。

    <name> **.bc** 。LLVM位码。

    <name> **.oc** : LLVM位码。WebAssembly 对象文件（除非使用 -flto，在这种情况下，它将是 LLVM 位码格式）。

    <name> **.wasm** : WebAssembly对象文件（除非使用-flto，否则它将是LLVM位码格式）。没有JavaScript支持代码的WebAssembly ("standalone wasm"；这将启用 "STANDALONE_WASM")。

注释

    如果使用"--memory-init-file"，除了生成**.js**和/或**.html**文件外，还将创建一个**.mem**文件。

### `-c`
告诉*emcc*生成LLVM位码（然后可以与其他位码文件链接），而不是一路编译到JavaScript。

### `--output_eol windows|linux`
指定要为输出的文本文件生成行尾。如果通过了"--output_eol windows"，最终的输出文件将以Windows rn行结尾。如果通过"--output_eol linux"，则最终生成的文件将以Unix n行结尾来编写。

### `--cflags`
打印出 "emcc "将传递给 "clang "的标志，以便将源代码编译成对象/位码形式。你可以用它来调用clang，然后在这些输出上运行 "emcc"，进行最后的链接+转换为JS。

环境变量
-----------------

环境变量对*emcc*的影响如下所示。

   * "EMMAKEN_JUST_CONFIGURE"

   * "EMMAKEN_CFLAGS"

   * "EMCC_DEBUG"

   * "EMCC_CLOSURE_ARGS" : 要传递给*Closure的参数。
     编译器*

在emcc.py中搜索 "os.environ"，看看这些是如何使用的。最有趣的可能是 "EMCC_DEBUG"，它强制编译器将构建文件和临时文件转储到一个临时目录中，以便审查。

------------------------------------------------------------------

emcc：支持的目标：llvm bitcode、javascript，而不是elf（autoconf喜欢看到上面的elf，以启用共享对象支持）。