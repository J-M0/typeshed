from typing import Literal, overload, type_check_only
from typing_extensions import TypeAlias

_Gateway: TypeAlias = tuple[str, str, bool]
_DefaultGateway: TypeAlias = tuple[str, str]

_KT: TypeAlias = int | Literal["default"]
_VT: TypeAlias = list[_Gateway] | dict[int, _DefaultGateway]

# At runtime, gateways() returns a normal dict that essentially
# has the type `dict[int, list[_Gateway]]`. However, it also has
# a "default" key that maps to a `dict[int, _DefaultGateway]`.
# A simple union doesn't express this well and is also ugly as
# sin, so these overloads let type checkers understand the
# which keys map to which types.
@type_check_only
class _Gateways(dict[_KT, _VT]):
    @overload
    def __getitem__(self, key: Literal["default"], /) -> dict[int, _DefaultGateway]: ...
    @overload
    def __getitem__(self, key: int, /) -> list[_Gateway]: ...
    @overload
    def __getitem__(self, key: _KT, /) -> _VT: ...  # This quiets errors about superclass signature mismatch

def gateways() -> _Gateways: ...
def ifaddresses(ifname: str, /) -> dict[int, list[dict[str, str]]]: ...
def interfaces() -> list[str]: ...

address_families: dict[int, str]
version: str

AF_12844: int
AF_APPLETALK: int
AF_ASH: int
AF_ATM: int
AF_ATMPVC: int
AF_ATMSVC: int
AF_AX25: int
AF_BAN: int
AF_BLUETOOTH: int
AF_BRIDGE: int
AF_CCITT: int
AF_CHAOS: int
AF_CLUSTER: int
AF_CNT: int
AF_COIP: int
AF_DATAKIT: int
AF_DECnet: int
AF_DLI: int
AF_ECMA: int
AF_ECONET: int
AF_FILE: int
AF_FIREFOX: int
AF_HYLINK: int
AF_IMPLINK: int
AF_INET6: int
AF_INET: int
AF_IPX: int
AF_IRDA: int
AF_ISDN: int
AF_ISO: int
AF_KEY: int
AF_LAT: int
AF_LINK: int
AF_NATM: int
AF_NDRV: int
AF_NETBEUI: int
AF_NETBIOS: int
AF_NETDES: int
AF_NETGRAPH: int
AF_NETLINK: int
AF_NETROM: int
AF_NS: int
AF_PACKET: int
AF_PPP: int
AF_PPPOX: int
AF_PUP: int
AF_ROSE: int
AF_ROUTE: int
AF_SECURITY: int
AF_SIP: int
AF_SNA: int
AF_SYSTEM: int
AF_UNIX: int
AF_UNKNOWN1: int
AF_UNSPEC: int
AF_VOICEVIEW: int
AF_WANPIPE: int
AF_X25: int
IN6_IFF_AUTOCONF: int
IN6_IFF_DYNAMIC: int
IN6_IFF_OPTIMISTIC: int
IN6_IFF_SECURED: int
IN6_IFF_TEMPORARY: int
