// http://eslint.org/docs/user-guide/configuring

module.exports = {
	root: true,
	parser: 'babel-eslint',
	parserOptions: {
		sourceType: 'module'
	},
	env: {
		browser: true,
	},
	// https://github.com/feross/standard/blob/master/RULES.md#javascript-standard-style
	extends: 'standard',
	// required to lint *.vue files
	plugins: [
		'html'
	],
	// add your custom rules here
	'rules': {
		// allow paren-less arrow functions
		'arrow-parens': 'off',
		// allow async-await
		'generator-star-spacing': 'off',
		// allow debugger during development
		'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
		// 'allowIndentationTabs': true,
		'indent': 'off',
		'no-tabs': 'off',
		'semi': ['error', "always"],
		'no-useless-return': 'off',
		'no-unused-vars': 'warn',
		'comma-dangle': 'off'
	},
	globals: {
		'$': true,
        'jQuery': true
	}
};
