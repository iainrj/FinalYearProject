import { h, Component } from 'preact';
import style from './style';

export default class Order extends Component {
	render() {
		return (
			<div class={style.order}>
				<table>
					<tr>
						<th class="tg-yw4l">Order</th>
						<th class="tg-yw4l">Country</th>
					</tr>
					<tr>
						<td class="tg-yw4l">1</td>
						<td class="tg-yw4l">Albania</td>
					</tr>
					<tr>
						<td class="tg-yw4l">2</td>
						<td class="tg-yw4l">Norway</td>
					</tr>
				</table>
			</div>
		);
	}
}
