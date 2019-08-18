<template>
	<div class="bg-white border">
		<editor-menu-bubble :editor="editor" @hide="hideLinkMenu">
			<div slot-scope="{ commands, isActive, getMarkAttrs, menu, linkMenuIsActive }">
				<div :class="{ 'active': menu.isActive }" :style="`left: ${menu.left}px; bottom: ${menu.bottom}px;`">
					<form v-if="linkMenuIsActive" @submit.prevent="setLinkUrl(commands.link, linkUrl)">
						<input type="text" v-model="linkUrl" placeholder="https://" ref="linkInput" @keydown.esc="hideLinkMenu"/>
						<button @click="setLinkUrl(commands.link, null)" type="button">
							<span class="fa fa-remove"></span>
						</button>
					</form>
				</div>
			</div>
		</editor-menu-bubble>

		<editor-menu-bar :editor="editor" class="border-bottom p-2 bg-dark">
			<div slot-scope="{ commands, isActive }">
				<div class="btn-group my-1">
					<button type="button" class="btn btn-sm btn-light dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
						<span class="fa fa-heading"></span>
					</button>
					<div class="dropdown-menu">
						<h1>
							<button :class="{ 'active': isActive.heading({ level: 1 }) }" @click="commands.heading({ level: 1 })" class="dropdown-item" type="button">Header 1</button>
						</h1>
						<h2>
							<button :class="{ 'active': isActive.heading({ level: 2 }) }" @click="commands.heading({ level: 2 })" class="dropdown-item" type="button">Header 2</button>
						</h2>
						<h3>
							<button :class="{ 'active': isActive.heading({ level: 3 }) }" @click="commands.heading({ level: 3 })" class="dropdown-item" type="button">Header 3</button>
						</h3>
						<h4>
							<button :class="{ 'active': isActive.heading({ level: 4 }) }" @click="commands.heading({ level: 4 })" class="dropdown-item" type="button">Header 4</button>
						</h4>
						<h5>
							<button :class="{ 'active': isActive.heading({ level: 5 }) }" @click="commands.heading({ level: 5 })" class="dropdown-item" type="button">Header 5</button>
						</h5>
						<h6>
							<button :class="{ 'active': isActive.heading({ level: 6 }) }" @click="commands.heading({ level: 6 })" class="dropdown-item" type="button">Header 6</button>
						</h6>
					</div>
				</div>

				<button :class="{ 'active': isActive.paragraph() }" @click="commands.paragraph" class="btn btn-sm btn-light my-1" type="button">
					<span class="fa fa-paragraph"></span>
				</button>

				<div class="btn-group my-1">
					<button :class="{ 'active': isActive.bold() }" @click="commands.bold" class="btn btn-sm btn-light" type="button">
						<span class="fa fa-bold"></span>
					</button>

					<button :class="{ 'active': isActive.italic() }" @click="commands.italic" class="btn btn-sm btn-light" type="button">
						<span class="fa fa-italic"></span>
					</button>

					<button :class="{ 'active': isActive.strike() }" @click="commands.strike" class="btn btn-sm btn-light" type="button">
						<span class="fa fa-strikethrough"></span>
					</button>

					<button :class="{ 'active': isActive.underline() }" @click="commands.underline" class="btn btn-sm btn-light" type="button">
						<span class="fa fa-underline"></span>
					</button>
				</div>

				<div class="btn-group my-1">
					<button :class="{ 'active': isActive.bullet_list() }" @click="commands.bullet_list" class="btn btn-sm btn-light" type="button">
						<span class="fa fa-list-ul"></span>
					</button>

					<button :class="{ 'active': isActive.ordered_list() }" @click="commands.ordered_list" class="btn btn-sm btn-light" type="button">
						<span class="fa fa-list-ol"></span>
					</button>
				</div>

				<button :class="{ 'active': isActive.link() }" @click="showLinkMenu(getMarkAttrs('link'))" class="btn btn-sm btn-light my-1" type="button">
					<span class="fa fa-link"></span>
				</button>

				<button :class="{ 'active': isActive.blockquote() }" @click="commands.blockquote" class="btn btn-sm btn-light my-1" type="button">
					<span class="fa fa-quote-left"></span>
				</button>

				<button @click="commands.horizontal_rule" class="btn btn-sm btn-light my-1" type="button">
					<span class="fa fa-minus"></span>
				</button>

				<button :class="{ 'active': isActive.todo_list() }" @click="commands.todo_list" class="btn btn-sm btn-light my-1" type="button">
					<span class="fa fa-tasks"></span>
				</button>

				<div class="btn-group my-1">
					<button @click="commands.undo" class="btn btn-sm btn-light" type="button">
						<span class="fa fa-undo"></span>
					</button>

					<button @click="commands.redo" class="btn btn-sm btn-light" type="button">
						<span class="fa fa-redo"></span>
					</button>
				</div>
			</div>
		</editor-menu-bar>

		<editor-content :editor="editor" class="p-3 tiptap-editor-content"/>
	</div>
</template>

<script>
	import {Editor, EditorContent, EditorMenuBar, EditorMenuBubble} from 'tiptap';
	import {
		Blockquote, Bold, BulletList, HardBreak, Heading, History, HorizontalRule,
		Image, Italic, Link, ListItem, OrderedList, Table, TableHeader,
		TableCell, TableRow, TodoItem, TodoList, Strike, Underline
	} from 'tiptap-extensions';

	export default {
		name: 'TipTap',
		components: {
			EditorContent,
			EditorMenuBar,
			EditorMenuBubble
		},
		props: {
			value: {
				type: String,
				default: ''
			}
		},
		data: function () {
			return {
				editor: new Editor({
					extensions: [
						new Blockquote(),
						new Bold(),
						new BulletList(),
						new HardBreak(),
						new Heading(),
						new History(),
						new HorizontalRule(),
						new Image(),
						new Italic(),
						new Link(),
						new ListItem(),
						new OrderedList(),
						new Table(),
						new TableHeader(),
						new TableCell(),
						new TableRow(),
						new TodoItem({
							nested: true
						}),
						new TodoList(),
						new Strike(),
						new Underline()
					],
					content: this.value,
					onUpdate: ({getHTML}) => {
						const state = getHTML();
						this.$emit('input', state);
					},
					linkUrl: null,
					linkMenuIsActive: false
				})
			};
		},
		methods: {
			showLinkMenu: function (attrs) {
				this.linkUrl = attrs.href;
				this.linkMenuIsActive = true;
				this.$nextTick(() => {
					this.$refs.linkInput.focus();
				});
			},
			hideLinkMenu: function () {
				this.linkUrl = null;
				this.linkMenuIsActive = false;
			},
			setLinkUrl: function (command, url) {
				command({href: url});
				this.hideLinkMenu();
			}
		},
		beforeDestroy: function () {
			this.editor.destroy();
		}
	};
</script>

<style>
	.tiptap-editor-content *:focus {
		outline: none;
	}

	.tiptap-editor-content > div {
		min-height: 400px;
	}

	ul[data-type="todo_list"] {
		padding-left: 0;
	}

	li[data-type="todo_item"] {
		display: flex;
		flex-direction: row;
	}

	.todo-checkbox {
		border: 2px solid black;
		height: 0.9em;
		width: 0.9em;
		box-sizing: border-box;
		margin-right: 10px;
		margin-top: 0.3rem;
		user-select: none;
		-webkit-user-select: none;
		cursor: pointer;
		border-radius: 0.2em;
		background-color: transparent;
		transition: 0.4s background;
	}

	.todo-content {
		flex: 1;
	}

	.todo-content > p:last-of-type {
		margin-bottom: 0;
	}

	.todo-content > ul[data-type="todo_list"] {
		margin: .5rem 0;
	}

	li[data-done="true"] > .todo-content > p {
		text-decoration: line-through;
	}

	li[data-done="true"] > .todo-checkbox {
		background-color: black;
	}

	li[data-done="false"] {
		text-decoration: none;
	}
</style>
