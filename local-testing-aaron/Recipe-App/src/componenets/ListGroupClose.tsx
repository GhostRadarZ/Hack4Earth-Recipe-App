// items []
interface Props {
    items: string[];
    onClose: () => void;
}

function ListGroupClose({items, onClose}: Props) {
    
   
    return (
    <>
        {items.length == 0 && <p> no items found </p>}
        <ul className="list-group">
            {items.map((item, index) => <li  className="list-group-item" key={item} onClick={() => console.log(item, index)}>{item} <button type="button" onClick={onClose} className="btn-close"></button> </li>)}
        </ul>
    </>
  );
}

export default ListGroupClose;