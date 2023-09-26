// items []
interface Props {
    items: string[];
}

function ListGroup({items}: Props) {
    
   
    return (
    <>
        {items.length == 0 && <p> no items found </p>}
        <ul className="list-group">
            {items.map((item, index) => <li  className="list-group-item" key={item} onClick={() => console.log(item, index)}>{item}</li>)}
        </ul>
    </>
  );
}

export default ListGroup;