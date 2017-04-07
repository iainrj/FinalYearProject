import { h, Component } from 'preact';
import style from './style';

export default class About extends Component {
	render() {
		return (
			<div class={style.About}>
				<h1>About</h1>
				<p>This is a project for a BSc in Computer Science final year project</p>
			</div>
		);
	}
}
