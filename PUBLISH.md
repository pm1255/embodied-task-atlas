# 上传 GitHub 并发布交互网页

仓库代码页展示 README 和预览图。交互网页由 GitHub Pages 提供，在 README 顶部与仓库 About 的 Website 字段放网页链接。

## 最少操作：浏览器上传

1. 在自己的 GitHub 账号或组织下创建空的公开仓库，例如 `embodied-task-atlas`。
2. 将本目录的内容上传到仓库根目录。不要把整个 `embodied-task-atlas` 文件夹再嵌套一层；根目录应直接看到 README.md、data、docs 等。
3. 在仓库 **Settings → Pages**，选择 **Deploy from a branch → main → /docs → Save**。
4. 等待 Pages 部署完成。以 Settings → Pages 实际显示的网址为准，通常为 `https://OWNER.github.io/embodied-task-atlas/`。
5. 在 README 顶部把“交互网页：待发布”替换为实际链接，并把同一网址放进仓库首页 About → Website。
6. 打开网址检查任务切换、B/G/P/GP、覆盖矩阵和最小子集。上线前后都应保留“文字规格，尚未模型测评”的状态。

发布准备时尚未选择许可证。正式作为开源项目发布前，维护者应确定代码与任务规格各自采用的许可，并加入对应 LICENSE 文件。

## 使用 Git 上传

先在 GitHub 创建空仓库。将下面的 OWNER 替换为真实账号或组织，不要原样执行占位符。

```bash
git init -b main
git add .
git commit -m "Add embodied task atlas and interactive explorer"
git remote add origin https://github.com/OWNER/embodied-task-atlas.git
git push -u origin main
```

在本项目目录内运行上述命令。推送需要本机已配置的 GitHub 登录或 Git 凭据；不要将 Token 写进仓库文件或远程 URL。

## 后续更新

```bash
python3 scripts/build.py
git add data/tasks.json docs/index.html docs/tasks.json
git commit -m "Update task catalog"
git push
```

Pages 发布源设为 main 的 /docs 后，推送这一目录中的修改会触发站点更新。此方案无需后端、数据库或额外主机。

GitHub 官方说明：
- https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
- https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site
