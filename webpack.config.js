const webpack = require('webpack');
const path = require('path');

/*
 * We've enabled UglifyJSPlugin for you! This minifies your app
 * in order to load faster and run less javascript.
 *
 * https://github.com/webpack-contrib/uglifyjs-webpack-plugin
 *
 */

module.exports = {
	entry: ['./static/js/main.js', './static/sass/main.scss'],

	output: {
		filename: 'bundle.js',
		path: path.resolve(__dirname, './static/dist')
	},

	module: {
        rules: [
            {
                test:/\.(s*)css$/,
                use:['style-loader', 'css-loader', 'sass-loader']
            },
            {
                test: /\.(png|jp(e*)g|svg)$/,
                use:[{
                    loader: 'url-loader',
                    options: {
                        limit: 8000,
                        name: 'img/[hash]-[name].[ext]'
                    }
                }]
            }
        ]
    },

    devServer: {
	    contentBase: path.resolve(__dirname, "./static/dist/assets/media"),
        open: true,
        port: 12000,
        stats: 'errors-only',
        compress: true
    },

    devtool: "inline-source-map"
};

